import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(BASE_DIR, "data", "processed", "retail_cleaned.csv")

df = pd.read_csv(csv_path)
df.columns = df.columns.str.strip()

print("Total Sales:",df['Sales_x'].sum())

print("Customers:",df['Customer ID'].nunique())

print("Orders:" ,df['Order ID'].nunique())