"""Rough Set Layer + RoughLSTM (real LSTM over raw window)."""
import torch
import torch.nn as nn

from config import (
    NUM_TIMESTEPS, NUM_AXES, NUM_FEATURES,
    LSTM_HIDDEN, LSTM_LAYERS, LSTM_DROPOUT,
    MLP_HIDDEN1, MLP_HIDDEN2, MLP_HIDDEN3, EPSILON,
)


class RoughSetLayer(nn.Module):
    def __init__(self, epsilon: float = 0.1):
        super().__init__()
        self.epsilon = epsilon

    def forward(self, x):
        probs = torch.softmax(x, dim=1)
        margin = torch.abs(probs[:, 1] - probs[:, 0])
        uncertainty = (margin / (2 * self.epsilon)).clamp(0, 1)
        return probs * uncertainty.unsqueeze(1)


class RoughLSTM(nn.Module):
   
    def __init__(
        self,
        num_timesteps: int = NUM_TIMESTEPS,
        num_axes: int = NUM_AXES,
        num_features: int = NUM_FEATURES,
        lstm_hidden: int = LSTM_HIDDEN,
        lstm_layers: int = LSTM_LAYERS,
        lstm_dropout: float = LSTM_DROPOUT,
        hidden1: int = MLP_HIDDEN1,
        hidden2: int = MLP_HIDDEN2,
        hidden3: int = MLP_HIDDEN3,
        num_classes: int = 2,
        epsilon: float = EPSILON,
    ):
        super().__init__()

        self.lstm = nn.LSTM(
            input_size=num_axes,
            hidden_size=lstm_hidden,
            num_layers=lstm_layers,
            batch_first=True,
            dropout=lstm_dropout if lstm_layers > 1 else 0.0,
            bidirectional=False,
        )

        combined = lstm_hidden + num_features

        self.fc1 = nn.Linear(combined, hidden1)
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

    def forward(self, x_seq, x_feat):
        lstm_out, _ = self.lstm(x_seq)          # (B, T, hidden)
        h_last = lstm_out[:, -1, :]             # (B, hidden)

        combined = torch.cat([h_last, x_feat], dim=1)

        x = self.drop1(self.relu(self.bn1(self.fc1(combined))))
        x = self.drop2(self.relu(self.bn2(self.fc2(x))))
        x = self.drop3(self.relu(self.bn3(self.fc3(x))))
        x = self.fc4(x)
        x = self.rough(x)
        return x