from pathlib import Path
import pandas as pd

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# File path
file_path = BASE_DIR / "data" / "processed" / "retail_cleaned.csv"

# Read data
df = pd.read_csv(file_path)

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Convert Order Date
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

# Create features
df["Month"] = df["Order Date"].dt.month_name()
df["Quarter"] = df["Order Date"].dt.quarter
df["Weekday"] = df["Order Date"].dt.day_name()

# Save back
df.to_csv(file_path, index=False)

print("Features Created")
print(f"Saved to: {file_path}")


#Verification
df = pd.read_csv("data/processed/retail_cleaned.csv")

print(df[['Order Date','Month','Quarter','Weekday']].head())
print()
print(df[['Month','Quarter','Weekday']].isna().sum())