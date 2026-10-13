"""
RoughLSTM 
Usage:
    python train_roughlstm_per_machine.py
"""

import os
import sys
import time
import random
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.fft import fft
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, confusion_matrix,
                             roc_auc_score, roc_curve, classification_report)

# ==========================================
# CONFIGURATION — Paper-Aligned
# ==========================================
MACHINES = ["M01", "M02", "M03"]

# Paper's selected operations for combined analysis
PAPER_OPS = ["OP02", "OP05", "OP08", "OP11", "OP14"]
LABELS = ["good", "bad"]

PATH_TO_DATASET = Path(r"C:\Users\T9943\project-1\data\raw")

# Windowing (matching paper)
WINDOW_SIZE = 50
OVERLAP = 25
STRIDE = WINDOW_SIZE - OVERLAP

# Model hyperparameters
WINDOWS_PER_FILE = 500
MAX_WINDOWS_PER_MACHINE = 80000
EPSILON = 0.1
BATCH_SIZE = 128
EPOCHS = 50
LEARNING_RATE = 0.001
PATIENCE = 10
NOISE_LEVEL = 0.05

# Reproducibility
SEED = 42
np.random.seed(SEED)
random.seed(SEED)
torch.manual_seed(SEED)

DEVICE = torch.device("cpu")
OUTPUT_DIR = Path(r"C:\Users\T9943\project-1\roughlstm_per_machine")
OUTPUT_DIR.mkdir(exist_ok=True)


# ==========================================
# 27-FEATURE EXTRACTION
# ==========================================
def extract_27_features(window):
    """9 canonical vibration features × 3 axes = 27."""
    features = []
    for axis in range(3):
        signal = window[:, axis]

        mean_val = np.mean(signal)
        std_val = np.std(signal)
        rms = np.sqrt(np.mean(signal ** 2))
        peak = np.max(np.abs(signal))
        peak_to_peak = np.max(signal) - np.min(signal)
        crest_factor = peak / (rms + 1e-8)
        skew = stats.skew(signal)
        kurt = stats.kurtosis(signal)

        fft_vals = np.abs(fft(signal))
        fft_vals = fft_vals[:len(fft_vals) // 2]
        dominant_bin = np.argmax(fft_vals)

        fft_norm = fft_vals / (np.sum(fft_vals) + 1e-8)
        spectral_entropy = -np.sum(fft_norm * np.log2(fft_norm + 1e-8))

        features.extend([
            mean_val, std_val, rms, crest_factor,
            peak_to_peak, dominant_bin, spectral_entropy,
            skew, kurt
        ])
    return np.array(features, dtype=np.float32)


# ==========================================
# FILE COLLECTION (per machine, paper OPs only)
# ==========================================
def collect_files_for_machine(machine):
    """Collect only paper's OP subset for one machine."""
    files = []
    for op in PAPER_OPS:
        for label in LABELS:
            folder = PATH_TO_DATASET / machine / op / label
            if not folder.exists():
                continue
            for csv_file in folder.glob("*.csv"):
                files.append({
                    "file_path": csv_file,
                    "machine": machine,
                    "op": op,
                    "label": label,
                })
    return files


# ==========================================
# FEATURE BUILDING
# ==========================================
def build_features(files):
    X, y = [], []
    t0 = time.time()

    for file_info in tqdm(files, desc="  Files"):
        try:
            df = pd.read_csv(file_info["file_path"])
            df = df[["x", "y", "z"]].dropna().reset_index(drop=True)
            if len(df) < WINDOW_SIZE:
                continue

            signal = df.values
            signal = (signal - np.mean(signal, axis=0)) / (np.std(signal, axis=0) + 1e-8)

            total = (len(signal) - WINDOW_SIZE) // STRIDE + 1
            if total <= 0:
                continue

            n_take = min(WINDOWS_PER_FILE, total)
            starts = np.random.choice(np.arange(total), size=n_take, replace=False)

            label_int = 1 if file_info["label"] == "good" else 0

            for s in starts:
                start = s * STRIDE
                window = signal[start:start + WINDOW_SIZE]
                X.append(extract_27_features(window))
                y.append(label_int)
        except Exception as e:
            print(f"  [ERROR] {file_info['file_path'].name}: {e}")

    X = np.array(X, dtype=np.float32)
    y = np.array(y, dtype=np.int64)
    print(f"  Extracted {X.shape[0]} windows in {(time.time()-t0)/60:.1f} min")
    print(f"  Class distribution: {np.bincount(y, minlength=2)}")
    return X, y


# ==========================================
# NOISE AUGMENTATION
# ==========================================
def augment_with_noise(X, y, noise_level=0.05):
    noise = np.random.normal(0, noise_level, X.shape).astype(np.float32)
    X_aug = X + noise
    return np.vstack([X, X_aug]), np.concatenate([y, y])


# ==========================================
# UNDERSAMPLE
# ==========================================
def undersample_train(X, y):
    idx_good = np.where(y == 1)[0]
    idx_bad = np.where(y == 0)[0]
    n = min(len(idx_good), len(idx_bad))
    np.random.shuffle(idx_good)
    np.random.shuffle(idx_bad)
    idx_bal = np.concatenate([idx_good[:n], idx_bad[:n]])
    np.random.shuffle(idx_bal)
    return X[idx_bal], y[idx_bal]


# ==========================================
# ROUGH SET LAYER
# ==========================================
class RoughSetLayer(nn.Module):
    def __init__(self, epsilon=0.1):
        super().__init__()
        self.epsilon = epsilon

    def forward(self, x):
        probs = torch.softmax(x, dim=1)
        margin = torch.abs(probs[:, 1] - probs[:, 0])
        uncertainty = (margin / (2 * self.epsilon)).clamp(0, 1)
        return probs * uncertainty.unsqueeze(1)


# ==========================================
# MODEL
# ==========================================
class RoughLSTM(nn.Module):
    def __init__(self, input_dim=27, hidden1=128, hidden2=64,
                 hidden3=32, num_classes=2, epsilon=0.1):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, hidden1)
        self.bn1 = nn.BatchNorm1d(hidden1)
        self.drop1 = nn.Dropout(0.4)

        self.fc2 = nn.Linear(hidden1, hidden2)
        self.bn2 = nn.BatchNorm1d(hidden2)
        self.drop2 = nn.Dropout(0.4)

        self.fc3 = nn.Linear(hidden2, hidden3)
        self.bn3 = nn.BatchNorm1d(hidden3)
        self.drop3 = nn.Dropout(0.3)

        self.fc4 = nn.Linear(hidden3, num_classes)
        self.rough = RoughSetLayer(epsilon=epsilon)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.drop1(self.relu(self.bn1(self.fc1(x))))
        x = self.drop2(self.relu(self.bn2(self.fc2(x))))
        x = self.drop3(self.relu(self.bn3(self.fc3(x))))
        x = self.fc4(x)
        x = self.rough(x)
        return x


class FeatureDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.long)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]


# ==========================================
# TRAIN
# ==========================================
def train_model(model, train_loader, val_loader, criterion, optimizer,
                epochs=50, patience=10):
    train_losses, val_losses = [], []
    train_accs, val_accs = [], []
    best_val_loss = float("inf")
    patience_ctr = 0
    best_state = None

    for epoch in range(epochs):
        model.train()
        run_loss, correct, total = 0.0, 0, 0
        for X_b, y_b in train_loader:
            X_b, y_b = X_b.to(DEVICE), y_b.to(DEVICE)
            optimizer.zero_grad()
            out = model(X_b)
            loss = criterion(out, y_b)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            run_loss += loss.item()
            _, pred = torch.max(out, 1)
            correct += (pred == y_b).sum().item()
            total += y_b.size(0)

        train_loss = run_loss / len(train_loader)
        train_acc = correct / total

        model.eval()
        v_loss, v_correct, v_total = 0.0, 0, 0
        preds_all, labels_all = [], []
        with torch.no_grad():
            for X_b, y_b in val_loader:
                X_b, y_b = X_b.to(DEVICE), y_b.to(DEVICE)
                out = model(X_b)
                v_loss += criterion(out, y_b).item()
                _, pred = torch.max(out, 1)
                v_correct += (pred == y_b).sum().item()
                v_total += y_b.size(0)
                preds_all.extend(pred.cpu().numpy())
                labels_all.extend(y_b.cpu().numpy())

        v_loss /= len(val_loader)
        v_acc = v_correct / v_total

        preds_all = np.array(preds_all)
        labels_all = np.array(labels_all)
        acc_good = accuracy_score(labels_all[labels_all == 1], preds_all[labels_all == 1]) \
            if (labels_all == 1).sum() > 0 else 0
        acc_bad = accuracy_score(labels_all[labels_all == 0], preds_all[labels_all == 0]) \
            if (labels_all == 0).sum() > 0 else 0

        train_losses.append(train_loss); val_losses.append(v_loss)
        train_accs.append(train_acc); val_accs.append(v_acc)

        print(f"  Epoch [{epoch+1:2d}/{epochs}] | "
              f"Train Loss: {train_loss:.4f} | Train Acc: {train_acc:.4f} | "
              f"Val Loss: {v_loss:.4f} | Val Acc: {v_acc:.4f} | "
              f"Good: {acc_good:.4f} | Bad: {acc_bad:.4f}")

        if v_loss < best_val_loss:
            best_val_loss = v_loss
            patience_ctr = 0
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
        else:
            patience_ctr += 1
            if patience_ctr >= patience:
                print(f"  Early stopping at epoch {epoch+1}.")
                model.load_state_dict(best_state)
                break

    return train_losses, val_losses, train_accs, val_accs


# ==========================================
# EVALUATE
# ==========================================
def evaluate(model, test_loader, machine_name):
    model.eval()
    preds, labels, probs = [], [], []
    with torch.no_grad():
        for X_b, y_b in test_loader:
            X_b, y_b = X_b.to(DEVICE), y_b.to(DEVICE)
            out = model(X_b)
            p = torch.softmax(out, dim=1)
            _, pred = torch.max(out, 1)
            preds.extend(pred.cpu().numpy())
            labels.extend(y_b.cpu().numpy())
            probs.extend(p[:, 1].cpu().numpy())

    preds = np.array(preds); labels = np.array(labels); probs = np.array(probs)

    acc = accuracy_score(labels, preds)
    auc = roc_auc_score(labels, probs)
    cm = confusion_matrix(labels, preds)

    print(f"\n  --- {machine_name} Test Results ---")
    print(f"  Accuracy: {acc:.4f} | AUC: {auc:.4f}")
    print(f"  Confusion Matrix:\n{cm}")
    print(classification_report(labels, preds,
                                target_names=["Anomalous", "Normal"]))

    # Confusion matrix plot
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=["Anomalous", "Normal"],
                yticklabels=["Anomalous", "Normal"])
    plt.title(f"Confusion Matrix — {machine_name}")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / f"confusion_{machine_name}.png", dpi=100)
    plt.close()

    # ROC curve
    fpr, tpr, _ = roc_curve(labels, probs)
    plt.figure(figsize=(7, 6))
    plt.plot(fpr, tpr, lw=2, label=f"{machine_name} (AUC = {auc:.3f})")
    plt.plot([0, 1], [0, 1], "k--", lw=1)
    plt.xlabel("False Positive Rate"); plt.ylabel("True Positive Rate")
    plt.title(f"ROC — {machine_name}")
    plt.legend(loc="lower right"); plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / f"roc_{machine_name}.png", dpi=100)
    plt.close()

    # Compute FPR & FNR
    tn, fp, fn, tp = cm.ravel()
    fpr_val = fp / (fp + tn) if (fp + tn) > 0 else 0
    fnr_val = fn / (fn + tp) if (fn + tp) > 0 else 0

    return {
        "machine": machine_name,
        "accuracy": acc,
        "auc": auc,
        "fpr": fpr_val,
        "fnr": fnr_val,
        "tp": int(tp), "tn": int(tn), "fp": int(fp), "fn": int(fn),
    }


# ==========================================
# TRAIN ONE MACHINE
# ==========================================
def run_machine(machine):
    print("\n" + "=" * 60)
    print(f"MACHINE {machine}")
    print("=" * 60)

    files = collect_files_for_machine(machine)
    print(f"  Files found: {len(files)}")

    if len(files) == 0:
        print(f"  No files for {machine}. Skipping.")
        return None

    # Count labels
    labels_list = [f["label"] for f in files]
    n_good = labels_list.count("good")
    n_bad = labels_list.count("bad")
    print(f"  Good files: {n_good} | Bad files: {n_bad}")

    # Extract features
    X, y = build_features(files)

    if len(X) < 100:
        print(f"  Not enough windows for {machine}. Skipping.")
        return None

    # Cap
    if len(X) > MAX_WINDOWS_PER_MACHINE:
        print(f"  Capping to {MAX_WINDOWS_PER_MACHINE} windows...")
        idx = np.random.choice(len(X), MAX_WINDOWS_PER_MACHINE, replace=False)
        X, y = X[idx], y[idx]
        print(f"  After cap: {X.shape}, classes: {np.bincount(y, minlength=2)}")

    # Check both classes present
    if len(np.unique(y)) < 2:
        print(f"  Only one class present for {machine}. Skipping.")
        return None

    # Split 70/15/15
    X_trainval, X_test, y_trainval, y_test = train_test_split(
        X, y, test_size=0.15, stratify=y, random_state=SEED)
    X_train, X_val, y_train, y_val = train_test_split(
        X_trainval, y_trainval, test_size=0.176, stratify=y_trainval,
        random_state=SEED)

    print(f"  Train: {X_train.shape} | Val: {X_val.shape} | Test: {X_test.shape}")
    print(f"  Train class dist: {np.bincount(y_train, minlength=2)}")

    # Augment + undersample train
    X_train_aug, y_train_aug = augment_with_noise(X_train, y_train, NOISE_LEVEL)
    X_train_bal, y_train_bal = undersample_train(X_train_aug, y_train_aug)
    print(f"  After augmentation + undersample: {X_train_bal.shape}, "
          f"classes: {np.bincount(y_train_bal, minlength=2)}")

    # Loaders
    train_loader = DataLoader(FeatureDataset(X_train_bal, y_train_bal),
                              batch_size=BATCH_SIZE, shuffle=True)
    val_loader = DataLoader(FeatureDataset(X_val, y_val),
                            batch_size=BATCH_SIZE, shuffle=False)
    test_loader = DataLoader(FeatureDataset(X_test, y_test),
                             batch_size=BATCH_SIZE, shuffle=False)

    # Model
    INPUT_DIM = X.shape[1]
    model = RoughLSTM(input_dim=INPUT_DIM, epsilon=EPSILON).to(DEVICE)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE, weight_decay=1e-5)

    # Train
    print(f"\n  Training {machine}...")
    train_losses, val_losses, train_accs, val_accs = train_model(
        model, train_loader, val_loader, criterion, optimizer,
        epochs=EPOCHS, patience=PATIENCE)

    # Learning curves
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    axes[0].plot(train_losses, label="Train")
    axes[0].plot(val_losses, label="Val")
    axes[0].set_title(f"{machine} — Loss")
    axes[0].legend(); axes[0].grid(alpha=0.3)
    axes[1].plot(train_accs, label="Train")
    axes[1].plot(val_accs, label="Val")
    axes[1].set_title(f"{machine} — Accuracy")
    axes[1].legend(); axes[1].grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / f"learning_curves_{machine}.png", dpi=100)
    plt.close()

    # Evaluate
    result = evaluate(model, test_loader, machine)

    # Save model
    torch.save(model.state_dict(), OUTPUT_DIR / f"roughlstm_{machine}.pt")

    return result


# ==========================================
# MAIN
# ==========================================
def main():
    print("\n" + "=" * 60)
    print("RoughLSTM — Paper Replication")
    print("Per-machine models on OP02+OP05+OP08+OP11+OP14")
    print("=" * 60)

    all_results = []
    t0 = time.time()

    for machine in MACHINES:
        result = run_machine(machine)
        if result is not None:
            all_results.append(result)

    # Final summary
    print("\n" + "=" * 60)
    print("FINAL SUMMARY — Paper Comparison")
    print("=" * 60)

    if not all_results:
        print("No results collected.")
        return

    summary_df = pd.DataFrame(all_results)
    summary_df = summary_df.round(4)
    print(summary_df.to_string(index=False))

    print(f"\nAverage across machines:")
    print(f"  Accuracy : {summary_df['accuracy'].mean():.4f}")
    print(f"  AUC-ROC  : {summary_df['auc'].mean():.4f}")
    print(f"  FPR      : {summary_df['fpr'].mean():.4f}")
    print(f"  FNR      : {summary_df['fnr'].mean():.4f}")

    print(f"\nPaper's reported results:")
    print(f"  Accuracy : 0.9430")
    print(f"  FPR      : 0.0370")
    print(f"  FNR      : 0.0200")

    summary_df.to_csv(OUTPUT_DIR / "final_summary.csv", index=False)
    print(f"\nTotal time: {(time.time()-t0)/60:.1f} min")
    print(f"Outputs saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()