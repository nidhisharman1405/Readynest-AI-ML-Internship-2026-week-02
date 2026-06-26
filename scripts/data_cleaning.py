from pathlib import Path
import pandas as pd

# Project root folder
BASE_DIR = Path(__file__).resolve().parent.parent

# File paths
input_file = BASE_DIR / "data" / "raw" / "store_sales_data (2).csv"
output_file = BASE_DIR / "data" / "processed" / "retail_cleaned.csv"

# Read data
df = pd.read_csv(input_file)

# Convert date columns
date_cols = ['Order Date', 'Ship Date', 'Sales Date', 'Date of Birth']

for col in date_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

# Save cleaned data
output_file.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_file, index=False)

print("Cleaning Completed")