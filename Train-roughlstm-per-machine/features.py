"""27 canonical vibration features per window (9 per axis)."""
import numpy as np
from scipy import stats
from scipy.fft import fft


def extract_27_features(window: np.ndarray) -> np.ndarray:
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
            skew, kurt,
        ])
    return np.array(features, dtype=np.float32)