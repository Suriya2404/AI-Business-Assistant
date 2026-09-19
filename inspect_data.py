import pandas as pd
from pathlib import Path

# Location of our raw Kaggle CSV files
data_folder = Path("data/raw")

# Find all CSV files
csv_files = list(data_folder.glob("*.csv"))

print(f"Found {len(csv_files)} CSV files.\n")

for file in csv_files:
    print("=" * 70)
    print(f"FILE: {file.name}")

    df = pd.read_csv(file)

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumns:")
    print(list(df.columns))

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nFirst 3 rows:")
    print(df.head(3))

    print()