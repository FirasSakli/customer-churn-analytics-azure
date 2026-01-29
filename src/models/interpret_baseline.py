from __future__ import annotations

from pathlib import Path

import joblib
import numpy as np
import pandas as pd


MODEL_PATH = Path("artifacts/baseline_model.joblib")
OUTPUT_PATH = Path("artifacts/baseline_feature_importance.csv")


def main() -> None:
    pipeline = joblib.load(MODEL_PATH)

    preprocessor = pipeline.named_steps["preprocess"]
    model = pipeline.named_steps["model"]

    # Get feature names
    cat_features = preprocessor.transformers_[0][2]
    num_features = preprocessor.transformers_[1][2]

    ohe = preprocessor.named_transformers_["cat"]
    cat_feature_names = ohe.get_feature_names_out(cat_features)

    feature_names = np.concatenate([cat_feature_names, num_features])

    coefs = model.coef_[0]

    importance = (
        pd.DataFrame(
            {
                "feature": feature_names,
                "coefficient": coefs,
                "odds_ratio": np.exp(coefs),
            }
        )
        .sort_values("odds_ratio", ascending=False)
        .reset_index(drop=True)
    )

    OUTPUT_PATH.parent.mkdir(exist_ok=True)
    importance.to_csv(OUTPUT_PATH, index=False)

    print("=== MODEL INTERPRETATION ===")
    print("Top positive churn drivers:")
    print(importance.head(10), "\n")

    print("Top negative churn drivers:")
    print(importance.tail(10))


if __name__ == "__main__":
    main()
