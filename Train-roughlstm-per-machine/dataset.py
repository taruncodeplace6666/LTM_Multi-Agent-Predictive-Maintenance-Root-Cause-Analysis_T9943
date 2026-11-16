"""Two-input dataset (raw window + 27 features)."""
import torch
from torch.utils.data import Dataset


class WindowDataset(Dataset):
    def __init__(self, X_seq, X_feat, y):
        self.X_seq = torch.tensor(X_seq, dtype=torch.float32)
        self.X_feat = torch.tensor(X_feat, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.long)

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        return self.X_seq[idx], self.X_feat[idx], self.y[idx]