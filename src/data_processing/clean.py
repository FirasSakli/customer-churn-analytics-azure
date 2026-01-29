from __future__ import annotations

from pathlib import Path

import pandas as pd


RAW_PATH = Path("data/raw/churn.csv")
SILVER_PATH = Path("data/processed/silver.parquet")


def load_raw_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Raw data not found at {path}")
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Standardize column names (optional but professional)
    df.columns = [c.strip() for c in df.columns]

    # Drop customer identifier (not predictive)
    if "customerID" in df.columns:
        df = df.drop(columns=["customerID"])

    # Convert churn to binary
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    # Convert TotalCharges to numeric (common issue in this dataset)
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Handle missing values
    # - numeric: median
    # - categorical: mode
    for col in df.columns:
        if df[col].dtype.kind in "if":  # numeric
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])

    return df


def main() -> None:
    df_raw = load_raw_data(RAW_PATH)
    df_silver = clean_data(df_raw)

    SILVER_PATH.parent.mkdir(parents=True, exist_ok=True)
    df_silver.to_parquet(SILVER_PATH, index=False)

    print("=== SILVER DATASET CREATED ===")
    print(f"Path: {SILVER_PATH}")
    print(f"Shape: {df_silver.shape}")
    print("\nDtypes:")
    print(df_silver.dtypes)
    print("\nChurn distribution:")
    print(df_silver["Churn"].value_counts(normalize=True))


if __name__ == "__main__":
    main()
