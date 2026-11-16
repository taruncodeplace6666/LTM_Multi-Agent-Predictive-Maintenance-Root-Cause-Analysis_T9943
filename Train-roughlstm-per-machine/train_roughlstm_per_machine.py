"""
RoughLSTM — Per-machine replication entry point.

Usage:
    python train_roughlstm_per_machine.py


Modules:
    config.py     – all constants
    features.py   – extract_27_features
    data.py       – file discovery, windowing, augmentation, undersampling
    models.py     – RoughSetLayer, RoughLSTM
    dataset.py    – two-input Dataset wrapper
    training.py   – training loop with early stopping
    evaluation.py – per-machine metrics + plots
    pipeline.py   – run_machine
    main.py       – loop over M01/M02/M03 + summary
"""
import os
import sys
import random
import warnings

import numpy as np
import torch

warnings.filterwarnings("ignore")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import SEED  # noqa: E402

np.random.seed(SEED)
random.seed(SEED)
torch.manual_seed(SEED)

from main import main  # noqa: E402

if __name__ == "__main__":
    main()