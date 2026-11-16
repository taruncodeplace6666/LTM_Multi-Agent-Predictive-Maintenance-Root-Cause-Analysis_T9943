"""Training loop with early stopping."""
import numpy as np
import torch
from sklearn.metrics import accuracy_score


def train_model(model, train_loader, val_loader, criterion, optimizer,
                device, epochs=50, patience=10):
    train_losses, val_losses = [], []
    train_accs, val_accs = [], []
    best_val_loss = float("inf")
    patience_ctr = 0
    best_state = None

    for epoch in range(epochs):
        # ----- Train -----
        model.train()
        run_loss, correct, total = 0.0, 0, 0

        for X_seq_b, X_feat_b, y_b in train_loader:
            X_seq_b = X_seq_b.to(device)
            X_feat_b = X_feat_b.to(device)
            y_b = y_b.to(device)

            optimizer.zero_grad()
            out = model(X_seq_b, X_feat_b)
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

        # ----- Validate -----
        model.eval()
        v_loss, v_correct, v_total = 0.0, 0, 0
        preds_all, labels_all = [], []

        with torch.no_grad():
            for X_seq_b, X_feat_b, y_b in val_loader:
                X_seq_b = X_seq_b.to(device)
                X_feat_b = X_feat_b.to(device)
                y_b = y_b.to(device)

                out = model(X_seq_b, X_feat_b)
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
        acc_good = (
            accuracy_score(labels_all[labels_all == 1], preds_all[labels_all == 1])
            if (labels_all == 1).sum() > 0 else 0
        )
        acc_bad = (
            accuracy_score(labels_all[labels_all == 0], preds_all[labels_all == 0])
            if (labels_all == 0).sum() > 0 else 0
        )

        train_losses.append(train_loss)
        val_losses.append(v_loss)
        train_accs.append(train_acc)
        val_accs.append(v_acc)

        print(
            f"  Epoch [{epoch + 1:2d}/{epochs}] | "
            f"Train Loss: {train_loss:.4f} | Train Acc: {train_acc:.4f} | "
            f"Val Loss: {v_loss:.4f} | Val Acc: {v_acc:.4f} | "
            f"Good: {acc_good:.4f} | Bad: {acc_bad:.4f}"
        )

        # ----- Early stopping -----
        if v_loss < best_val_loss:
            best_val_loss = v_loss
            patience_ctr = 0
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
        else:
            patience_ctr += 1
            if patience_ctr >= patience:
                print(f"  Early stopping at epoch {epoch + 1}.")
                model.load_state_dict(best_state)
                break

    return train_losses, val_losses, train_accs, val_accs