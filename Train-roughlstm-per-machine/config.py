"""All constants for the per-machine RoughLSTM pipeline."""
from pathlib import Path

# ---------- Data ----------
MACHINES = ["M01", "M02", "M03"]
PAPER_OPS = ["OP02", "OP05", "OP08", "OP11", "OP14"]
LABELS = ["good", "bad"]

PATH_TO_DATASET = Path(r"C:\Users\T9943\project-1\data\raw")
OUTPUT_DIR = Path(r"C:\Users\T9943\project-1\roughlstm_per_machine")
OUTPUT_DIR.mkdir(exist_ok=True)

# ---------- Windowing ----------
WINDOW_SIZE = 50
OVERLAP = 25
STRIDE = WINDOW_SIZE - OVERLAP

WINDOWS_PER_FILE = 500
MAX_WINDOWS_PER_MACHINE = 80000

# ---------- Feature / model dims ----------
NUM_FEATURES = 27
NUM_TIMESTEPS = WINDOW_SIZE
NUM_AXES = 3

# ---------- Model hyperparameters ----------
EPSILON = 0.1

LSTM_HIDDEN = 128
LSTM_LAYERS = 2
LSTM_DROPOUT = 0.3

MLP_HIDDEN1 = 128
MLP_HIDDEN2 = 64
MLP_HIDDEN3 = 32

BATCH_SIZE = 128
EPOCHS = 50
LEARNING_RATE = 0.001
PATIENCE = 10
NOISE_LEVEL = 0.05

# ---------- Reproducibility ----------
SEED = 42