"""Per-machine test metrics + plots."""
import numpy as np
import torch
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    accuracy_score, confusion_matrix, roc_auc_score,
    roc_curve, classification_report,
)


def evaluate(model, test_loader, device, machine_name, output_dir):
    model.eval()
    preds, labels, probs = [], [], []

    with torch.no_grad():
        for X_seq_b, X_feat_b, y_b in test_loader:
            X_seq_b = X_seq_b.to(device)
            X_feat_b = X_feat_b.to(device)
            y_b = y_b.to(device)

            out = model(X_seq_b, X_feat_b)
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

    print(f"\n  --- {machine_name} Test Results ---")
    print(f"  Accuracy: {acc:.4f} | AUC: {auc:.4f}")
    print(f"  Confusion Matrix:\n{cm}")
    print(classification_report(
        labels, preds, target_names=["Anomalous", "Normal"]
    ))

    # ----- Confusion matrix plot -----
    plt.figure(figsize=(6, 5))
    sns.heatmap(
        cm, annot=True, fmt="d", cmap="Blues",
        xticklabels=["Anomalous", "Normal"],
        yticklabels=["Anomalous", "Normal"],
    )
    plt.title(f"Confusion Matrix — {machine_name}")
    plt.tight_layout()
    plt.savefig(output_dir / f"confusion_{machine_name}.png", dpi=100)
    plt.close()

    # ----- ROC curve -----
    fpr, tpr, _ = roc_curve(labels, probs)
    plt.figure(figsize=(7, 6))
    plt.plot(fpr, tpr, lw=2, label=f"{machine_name} (AUC = {auc:.3f})")
    plt.plot([0, 1], [0, 1], "k--", lw=1)
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title(f"ROC — {machine_name}")
    plt.legend(loc="lower right")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_dir / f"roc_{machine_name}.png", dpi=100)
    plt.close()

    # ----- FPR / FNR -----
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