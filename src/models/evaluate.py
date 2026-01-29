from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix


DATA_PATH = Path("data/processed/silver.parquet")
MODEL_PATH = Path("artifacts/baseline_model.joblib")


def main() -> None:
    df = pd.read_parquet(DATA_PATH)

    X = df.drop(columns=["Churn"])
    y = df["Churn"]

    model = joblib.load(MODEL_PATH)

    y_pred = model.predict(X)

    print("=== BASELINE MODEL EVALUATION ===")
    print("\nConfusion Matrix:")
    print(confusion_matrix(y, y_pred))

    print("\nClassification Report:")
    print(classification_report(y, y_pred))


if __name__ == "__main__":
    main()
