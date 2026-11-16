"""Per-machine training pipeline."""
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader
from sklearn.model_selection import train_test_split

from config import (
    OUTPUT_DIR, MAX_WINDOWS_PER_MACHINE, BATCH_SIZE,
    EPOCHS, LEARNING_RATE, PATIENCE, NOISE_LEVEL, EPSILON, SEED,
)
from data import (
    collect_files_for_machine, build_sequences,
    augment_with_noise, undersample_train,
)
from dataset import WindowDataset
from models import RoughLSTM
from training import train_model
from evaluation import evaluate

DEVICE = torch.device("cpu")


def run_machine(machine):
    print("\n" + "=" * 60)
    print(f"MACHINE {machine}")
    print("=" * 60)

    files = collect_files_for_machine(machine)
    print(f"  Files found: {len(files)}")

    if len(files) == 0:
        print(f"  No files for {machine}. Skipping.")
        return None

    labels_list = [f["label"] for f in files]
    n_good = labels_list.count("good")
    n_bad = labels_list.count("bad")
    print(f"  Good files: {n_good} | Bad files: {n_bad}")

    # ---- Build raw windows + features ----
    X_seq, X_feat, y = build_sequences(files)

    if len(y) < 100:
        print(f"  Not enough windows for {machine}. Skipping.")
        return None

    # ---- Cap ----
    if len(y) > MAX_WINDOWS_PER_MACHINE:
        print(f"  Capping to {MAX_WINDOWS_PER_MACHINE} windows...")
        idx = np.random.choice(len(y), MAX_WINDOWS_PER_MACHINE, replace=False)
        X_seq, X_feat, y = X_seq[idx], X_feat[idx], y[idx]
        print(f"  After cap: {X_seq.shape}, classes: {np.bincount(y, minlength=2)}")

    if len(np.unique(y)) < 2:
        print(f"  Only one class present for {machine}. Skipping.")
        return None

    # ---- Stratified 70 / 15 / 15 split ----
    X_seq_tv, X_seq_te, X_feat_tv, X_feat_te, y_tv, y_te = train_test_split(
        X_seq, X_feat, y,
        test_size=0.15, stratify=y, random_state=SEED,
    )
    X_seq_tr, X_seq_va, X_feat_tr, X_feat_va, y_tr, y_va = train_test_split(
        X_seq_tv, X_feat_tv, y_tv,
        test_size=0.176, stratify=y_tv, random_state=SEED,
    )

    print(f"  Train: {X_seq_tr.shape} | Val: {X_seq_va.shape} | Test: {X_seq_te.shape}")
    print(f"  Train class dist: {np.bincount(y_tr, minlength=2)}")

    # ---- Augment + undersample train only ----
    X_seq_tr_aug, X_feat_tr_aug, y_tr_aug = augment_with_noise(
        X_seq_tr, X_feat_tr, y_tr, NOISE_LEVEL,
    )
    X_seq_bal, X_feat_bal, y_bal = undersample_train(
        X_seq_tr_aug, X_feat_tr_aug, y_tr_aug,
    )
    print(f"  After augmentation + undersample: {X_seq_bal.shape}, "
          f"classes: {np.bincount(y_bal, minlength=2)}")

    # ---- DataLoaders ----
    train_loader = DataLoader(
        WindowDataset(X_seq_bal, X_feat_bal, y_bal),
        batch_size=BATCH_SIZE, shuffle=True,
    )
    val_loader = DataLoader(
        WindowDataset(X_seq_va, X_feat_va, y_va),
        batch_size=BATCH_SIZE, shuffle=False,
    )
    test_loader = DataLoader(
        WindowDataset(X_seq_te, X_feat_te, y_te),
        batch_size=BATCH_SIZE, shuffle=False,
    )

    # ---- Model ----
    model = RoughLSTM(epsilon=EPSILON).to(DEVICE)
    print(f"  Model params: {sum(p.numel() for p in model.parameters()):,}")

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE, weight_decay=1e-5)

    # ---- Train ----
    print(f"\n  Training {machine}...")
    train_losses, val_losses, train_accs, val_accs = train_model(
        model, train_loader, val_loader, criterion, optimizer,
        device=DEVICE, epochs=EPOCHS, patience=PATIENCE,
    )

    # ---- Learning curves ----
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

    # ---- Evaluate ----
    result = evaluate(model, test_loader, DEVICE, machine, OUTPUT_DIR)

    # ---- Save model ----
    torch.save(model.state_dict(), OUTPUT_DIR / f"roughlstm_{machine}.pt")

    return result