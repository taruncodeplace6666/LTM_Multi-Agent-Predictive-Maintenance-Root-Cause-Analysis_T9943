"""Orchestrates per-machine training + final summary."""
import time
import pandas as pd

from config import MACHINES, OUTPUT_DIR
from pipeline import run_machine


def main():
    print("\n" + "=" * 60)
    print("RoughLSTM — Paper Replication (real LSTM + Rough Set)")
    print("Per-machine models on OP02+OP05+OP08+OP11+OP14")
    print("=" * 60)

    all_results = []
    t0 = time.time()

    for machine in MACHINES:
        result = run_machine(machine)
        if result is not None:
            all_results.append(result)

    print("\n" + "=" * 60)
    print("FINAL SUMMARY — Paper Comparison")
    print("=" * 60)

    if not all_results:
        print("No results collected.")
        return

    summary_df = pd.DataFrame(all_results).round(4)
    print(summary_df.to_string(index=False))

    print("\nAverage across machines:")
    print(f"  Accuracy : {summary_df['accuracy'].mean():.4f}")
    print(f"  AUC-ROC  : {summary_df['auc'].mean():.4f}")
    print(f"  FPR      : {summary_df['fpr'].mean():.4f}")
    print(f"  FNR      : {summary_df['fnr'].mean():.4f}")

    print("\nPaper's reported results:")
    print("  Accuracy : 0.9430")
    print("  FPR      : 0.0370")
    print("  FNR      : 0.0200")

    summary_df.to_csv(OUTPUT_DIR / "final_summary.csv", index=False)
    print(f"\nTotal time: {(time.time() - t0) / 60:.1f} min")
    print(f"Outputs saved to: {OUTPUT_DIR}")