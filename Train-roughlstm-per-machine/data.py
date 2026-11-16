"""File collection, raw-window + feature extraction, augmentation, undersampling."""
import time
import numpy as np
import pandas as pd
from tqdm import tqdm

from config import (
    PAPER_OPS, LABELS, PATH_TO_DATASET,
    WINDOW_SIZE, STRIDE, WINDOWS_PER_FILE,
)
from features import extract_27_features


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


def build_sequences(files):
    """
    Returns
        X_seq  : (N, WINDOW_SIZE, 3) raw normalized windows (LSTM input)
        X_feat : (N, 27) handcrafted features (MLP branch input)
        y      : (N,) int labels (1=good, 0=bad)
    """
    X_seq, X_feat, y = [], [], []
    t0 = time.time()

    for file_info in tqdm(files, desc="  Files"):
        try:
            df = pd.read_csv(file_info["file_path"])
            df = df[["x", "y", "z"]].dropna().reset_index(drop=True)
            if len(df) < WINDOW_SIZE:
                continue

            signal = df.values
            signal = (signal - np.mean(signal, axis=0)) / (
                np.std(signal, axis=0) + 1e-8
            )

            total = (len(signal) - WINDOW_SIZE) // STRIDE + 1
            if total <= 0:
                continue

            n_take = min(WINDOWS_PER_FILE, total)
            starts = np.random.choice(np.arange(total), size=n_take, replace=False)

            label_int = 1 if file_info["label"] == "good" else 0

            for s in starts:
                start = s * STRIDE
                window = signal[start:start + WINDOW_SIZE]          # (50, 3)
                feats = extract_27_features(window)                 # (27,)
                X_seq.append(window.astype(np.float32))
                X_feat.append(feats)
                y.append(label_int)
        except Exception as e:
            print(f"  [ERROR] {file_info['file_path'].name}: {e}")

    X_seq = np.array(X_seq, dtype=np.float32)
    X_feat = np.array(X_feat, dtype=np.float32)
    y = np.array(y, dtype=np.int64)

    print(f"  Extracted {X_seq.shape[0]} windows in {(time.time() - t0) / 60:.1f} min")
    print(f"  X_seq:  {X_seq.shape}")
    print(f"  X_feat: {X_feat.shape}")
    print(f"  Class distribution: {np.bincount(y, minlength=2)}")
    return X_seq, X_feat, y


def augment_with_noise(X_seq, X_feat, y, noise_level=0.05):
    """Append Gaussian-noise copies of every sample (paper approach)."""
    noise_seq = np.random.normal(0, noise_level, X_seq.shape).astype(np.float32)
    noise_feat = np.random.normal(0, noise_level, X_feat.shape).astype(np.float32)

    X_seq_out = np.concatenate([X_seq, X_seq + noise_seq], axis=0)
    X_feat_out = np.concatenate([X_feat, X_feat + noise_feat], axis=0)
    y_out = np.concatenate([y, y], axis=0)
    return X_seq_out, X_feat_out, y_out


def undersample_train(X_seq, X_feat, y):
    """Match minority class count on training data only."""
    idx_good = np.where(y == 1)[0]
    idx_bad = np.where(y == 0)[0]
    n = min(len(idx_good), len(idx_bad))

    np.random.shuffle(idx_good)
    np.random.shuffle(idx_bad)

    idx_bal = np.concatenate([idx_good[:n], idx_bad[:n]])
    np.random.shuffle(idx_bal)

    return X_seq[idx_bal], X_feat[idx_bal], y[idx_bal]