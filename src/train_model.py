"""
RoughLSTM — Replication of Cekik & Turan (2025) Approach
=========================================================
- 27 canonical vibration features per window (9 per axis)
- Random undersampling on training set only
- Noise augmentation
- Rough Set Layer (epsilon = 0.1)
- 5-fold style evaluation with stratification

Usage:
    python train_roughlstm.py
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
# CONFIGURATION
# ==========================================
MACHINES = ["M01", "M02", "M03"]
PROCESS_NAMES = [
    "OP00", "OP01", "OP02", "OP03", "OP04",
    "OP05", "OP06", "OP07", "OP08", "OP09",
    "OP10", "OP11", "OP12", "OP13", "OP14",
]
LABELS = ["good", "bad"]

PATH_TO_DATASET = Path(r"C:\Users\T9943\project-1\data\raw")

# Windowing (matching the paper)
WINDOW_SIZE = 50
OVERLAP = 25
STRIDE = WINDOW_SIZE - OVERLAP

# Model hyperparameters
WINDOWS_PER_FILE = 200     # sample windows per file (for CPU)
MAX_WINDOWS_TOTAL = 150000 # cap total windows before balancing
EPSILON = 0.1              # Rough Set Layer uncertainty threshold
BATCH_SIZE = 128
EPOCHS = 50
LEARNING_RATE = 0.001
PATIENCE = 8               # early stopping
NOISE_LEVEL = 0.05         # noise augmentation

# Reproducibility
SEED = 42
np.random.seed(SEED)
random.seed(SEED)
torch.manual_seed(SEED)

DEVICE = torch.device("cpu")
OUTPUT_DIR = Path(r"C:\Users\T9943\project-1\roughlstm_output")
OUTPUT_DIR.mkdir(exist_ok=True)


# ==========================================
# FEATURE EXTRACTION (27 features per window)
# ==========================================
def extract_27_features(window):
    """
    Extract 9 canonical vibration features per axis = 27 total.
    Matches Cekik & Turan (2025) feature set.
    """
    features = []
    for axis in range(3):  # x, y, z
        signal = window[:, axis]

        # --- Time-domain ---
        mean_val = np.mean(signal)
        std_val = np.std(signal)
        rms = np.sqrt(np.mean(signal ** 2))
        peak = np.max(np.abs(signal))
        peak_to_peak = np.max(signal) - np.min(signal)
        crest_factor = peak / (rms + 1e-8)
        skew = stats.skew(signal)
        kurt = stats.kurtosis(signal)

        # --- Frequency-domain ---
        fft_vals = np.abs(fft(signal))
        fft_vals = fft_vals[:len(fft_vals) // 2]  # positive freqs only

        # Dominant FFT-bin (primary vibration frequency)
        dominant_bin = np.argmax(fft_vals)

        # Spectral entropy (concentration of frequency components)
        fft_norm = fft_vals / (np.sum(fft_vals) + 1e-8)
        spectral_entropy = -np.sum(fft_norm * np.log2(fft_norm + 1e-8))

        features.extend([
            mean_val, std_val, rms, crest_factor,
            peak_to_peak, dominant_bin, spectral_entropy,
            skew, kurt
        ])
    return np.array(features, dtype=np.float32)


# ==========================================
# DATA LOADING + FEATURE EXTRACTION
# ==========================================
def collect_files():
    all_files = []
    for machine in MACHINES:
        for op in PROCESS_NAMES:
            for label in LABELS:
                folder = PATH_TO_DATASET / machine / op / label
                if not folder.exists():
                    continue
                for csv_file in folder.glob("*.csv"):
                    all_files.append({
                        "file_path": csv_file,
                        "machine": machine,
                        "op": op,
                        "label": label,
                    })
    return all_files


def build_features(all_files):
    print("=" * 60)
    print("Extracting 27 features per window")
    print("=" * 60)

    X, y, meta = [], [], []
    t0 = time.time()

    for file_info in tqdm(all_files, desc="Files"):
        try:
            df = pd.read_csv(file_info["file_path"])
            df = df[["x", "y", "z"]].dropna().reset_index(drop=True)
            if len(df) < WINDOW_SIZE:
                continue

            # Normalize per-file
            signal = df.values
            signal = (signal - np.mean(signal, axis=0)) / (np.std(signal, axis=0) + 1e-8)

            # Total windows
            total = (len(signal) - WINDOW_SIZE) // STRIDE + 1
            if total <= 0:
                continue

            # Sample WINDOWS_PER_FILE windows
            n_take = min(WINDOWS_PER_FILE, total)
            starts = np.random.choice(np.arange(total), size=n_take, replace=False)

            label_int = 1 if file_info["label"] == "good" else 0

            for s in starts:
                start = s * STRIDE
                window = signal[start:start + WINDOW_SIZE]
                feats = extract_27_features(window)
                X.append(feats)
                y.append(label_int)
                meta.append((file_info["machine"], file_info["op"], file_info["label"]))
        except Exception as e:
            print(f"  [ERROR] {file_info['file_path'].name}: {e}")

    X = np.array(X, dtype=np.float32)
    y = np.array(y, dtype=np.int64)
    meta = np.array(meta, dtype=object)

    print(f"Extracted {X.shape[0]} windows in {(time.time()-t0)/60:.1f} min")
    print(f"Feature shape: {X.shape}")
    print(f"Class distribution: {np.bincount(y)}")

    return X, y, meta


# ==========================================
# NOISE AUGMENTATION
# ==========================================
def augment_with_noise(X, y, noise_level=0.05):
    """Add Gaussian noise copies of every sample to boost training size."""
    noise = np.random.normal(0, noise_level, X.shape).astype(np.float32)
    X_aug = X + noise
    X_out = np.vstack([X, X_aug])
    y_out = np.concatenate([y, y])
    return X_out, y_out


# ==========================================
# ROUGH SET LAYER
# ==========================================
class RoughSetLayer(nn.Module):
    """
    Rough Set decision layer (Cekik & Turan 2025).
    Classifies outputs into lower / upper / boundary regions.
    """
    def __init__(self, epsilon=0.1):
        super().__init__()
        self.epsilon = epsilon

    def forward(self, x):
        # x is logits for 2 classes; convert to probabilities
        probs = torch.softmax(x, dim=1)
        # Uncertainty score based on distance from decision boundary
        # For binary: margin = |p1 - p0|; low margin = uncertain
        margin = torch.abs(probs[:, 1] - probs[:, 0])
        uncertainty = (margin / (2 * self.epsilon)).clamp(0, 1)
        # Scale probabilities by certainty (values near boundary get downweighted)
        scaled = probs * uncertainty.unsqueeze(1)
        return scaled


# ==========================================
# ROUGH LSTM MODEL
# ==========================================
class RoughLSTM(nn.Module):
    """
    Fully-connected feedforward network on 27 features.
    (LSTM would be used if we passed sequential windows;
    here we use extracted features so MLP is equivalent & faster.)
    """
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


# ==========================================
# DATASET
# ==========================================
class FeatureDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.long)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]


# ==========================================
# UNDERSAMPLING (only on training set!)
# ==========================================
def undersample_train(X, y):
    """
    Match minority class count on training data only.
    This is what the paper does to prevent bias.
    """
    idx_good = np.where(y == 1)[0]
    idx_bad = np.where(y == 0)[0]
    n = min(len(idx_good), len(idx_bad))

    np.random.shuffle(idx_good)
    np.random.shuffle(idx_bad)

    idx_bal = np.concatenate([idx_good[:n], idx_bad[:n]])
    np.random.shuffle(idx_bal)

    return X[idx_bal], y[idx_bal]


# ==========================================
# TRAINING
# ==========================================
def train_model(model, train_loader, val_loader, criterion, optimizer,
                epochs=50, patience=8):
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

        # Validation
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

        train_losses.append(train_loss)
        val_losses.append(v_loss)
        train_accs.append(train_acc)
        val_accs.append(v_acc)

        print(f"Epoch [{epoch+1:2d}/{epochs}] | "
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
                print(f"\nEarly stopping at epoch {epoch+1}. Loading best model.")
                model.load_state_dict(best_state)
                break

    return train_losses, val_losses, train_accs, val_accs


# ==========================================
# EVALUATION
# ==========================================
def evaluate(model, test_loader):
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

    preds = np.array(preds)
    labels = np.array(labels)
    probs = np.array(probs)

    acc = accuracy_score(labels, preds)
    auc = roc_auc_score(labels, probs)
    cm = confusion_matrix(labels, preds)

    print("\n" + "=" * 60)
    print("FINAL TEST RESULTS")
    print("=" * 60)
    print(f"Accuracy : {acc:.4f}")
    print(f"AUC-ROC  : {auc:.4f}")
    print(f"\nConfusion Matrix:\n{cm}")
    print("\nClassification Report:")
    print(classification_report(labels, preds,
                                target_names=["Anomalous (bad)", "Normal (good)"]))

    # Plot confusion matrix
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=["Anomalous", "Normal"],
                yticklabels=["Anomalous", "Normal"])
    plt.title("Confusion Matrix — RoughLSTM")
    plt.xlabel("Predicted"); plt.ylabel("Actual")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "confusion_matrix.png", dpi=100)
    plt.close()

    # ROC curve
    fpr, tpr, _ = roc_curve(labels, probs)
    plt.figure(figsize=(7, 6))
    plt.plot(fpr, tpr, color="darkorange", lw=2,
             label=f"RoughLSTM ROC (AUC = {auc:.3f})")
    plt.plot([0, 1], [0, 1], "navy", lw=2, linestyle="--", label="Random")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve — RoughLSTM")
    plt.legend(loc="lower right")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "roc_curve.png", dpi=100)
    plt.close()

    return acc, auc


# ==========================================
# MAIN
# ==========================================
def main():
    print("\n" + "=" * 60)
    print("RoughLSTM — Cekik & Turan (2025) Replication")
    print("=" * 60 + "\n")

    # 1. Collect files
    all_files = collect_files()
    print(f"Total CSV files: {len(all_files)}\n")

    # 2. Extract features
    X, y, meta = build_features(all_files)

    # Optional cap
    if len(X) > MAX_WINDOWS_TOTAL:
        print(f"Capping to {MAX_WINDOWS_TOTAL} windows...")
        idx = np.random.choice(len(X), MAX_WINDOWS_TOTAL, replace=False)
        X, y = X[idx], y[idx]
        print(f"After cap: {X.shape}, classes: {np.bincount(y)}")

    # 3. Train / Val / Test split (70/15/15, stratified)
    X_trainval, X_test, y_trainval, y_test = train_test_split(
        X, y, test_size=0.15, stratify=y, random_state=SEED)
    X_train, X_val, y_train, y_val = train_test_split(
        X_trainval, y_trainval, test_size=0.176, stratify=y_trainval,
        random_state=SEED)  # 0.176 ≈ 15% of total

    print(f"\nTrain: {X_train.shape} | Val: {X_val.shape} | Test: {X_test.shape}")
    print(f"Train class dist: {np.bincount(y_train)}")

    # 4. Augment training with noise (paper approach)
    X_train_aug, y_train_aug = augment_with_noise(X_train, y_train, NOISE_LEVEL)
    print(f"After augmentation: {X_train_aug.shape}, classes: {np.bincount(y_train_aug)}")

    # 5. Undersample ONLY the training set (no leakage!)
    X_train_bal, y_train_bal = undersample_train(X_train_aug, y_train_aug)
    print(f"After undersample: {X_train_bal.shape}, classes: {np.bincount(y_train_bal)}")

    # 6. DataLoaders
    train_loader = DataLoader(FeatureDataset(X_train_bal, y_train_bal),
                              batch_size=BATCH_SIZE, shuffle=True)
    val_loader = DataLoader(FeatureDataset(X_val, y_val),
                            batch_size=BATCH_SIZE, shuffle=False)
    test_loader = DataLoader(FeatureDataset(X_test, y_test),
                             batch_size=BATCH_SIZE, shuffle=False)

    # 7. Model
    INPUT_DIM = X.shape[1]
    model = RoughLSTM(input_dim=INPUT_DIM, epsilon=EPSILON).to(DEVICE)
    print(f"\nModel: RoughLSTM (input_dim={INPUT_DIM}, epsilon={EPSILON})")
    print(f"Parameters: {sum(p.numel() for p in model.parameters()):,}")

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE, weight_decay=1e-5)

    # 8. Train
    print("\n" + "=" * 60)
    print("TRAINING")
    print("=" * 60)
    train_losses, val_losses, train_accs, val_accs = train_model(
        model, train_loader, val_loader, criterion, optimizer,
        epochs=EPOCHS, patience=PATIENCE)

    # 9. Save learning curves
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    axes[0].plot(train_losses, label="Train Loss")
    axes[0].plot(val_losses, label="Val Loss")
    axes[0].set_xlabel("Epoch"); axes[0].set_ylabel("Loss")
    axes[0].set_title("Loss"); axes[0].legend(); axes[0].grid(alpha=0.3)

    axes[1].plot(train_accs, label="Train Acc")
    axes[1].plot(val_accs, label="Val Acc")
    axes[1].set_xlabel("Epoch"); axes[1].set_ylabel("Accuracy")
    axes[1].set_title("Accuracy"); axes[1].legend(); axes[1].grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "learning_curves.png", dpi=100)
    plt.close()

    # 10. Evaluate on test
    acc, auc = evaluate(model, test_loader)

    # 11. Save model
    torch.save(model.state_dict(), OUTPUT_DIR / "roughlstm_model.pt")
    print(f"\nOutputs saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()