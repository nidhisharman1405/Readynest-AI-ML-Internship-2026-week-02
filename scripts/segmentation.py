from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

input_file = BASE_DIR / "data" / "processed" / "retail_cleaned.csv"
output_file = BASE_DIR / "outputs" / "csv" / "customer_segments.csv"

df = pd.read_csv(input_file)
df.columns = df.columns.str.strip()

sales_col = "Sales_y"      # Change to Sales_x if that's the correct one

customer_sales = (
    df.groupby("Customer ID")[sales_col]
      .sum()
      .reset_index()
)

customer_sales.rename(columns={sales_col: "Sales"}, inplace=True)

high = customer_sales["Sales"].quantile(0.80)
medium = customer_sales["Sales"].quantile(0.40)

def classify(x):
    if x >= high:
        return "High Value"
    elif x >= medium:
        return "Medium Value"
    return "Low Value"

customer_sales["Customer Segment"] = customer_sales["Sales"].apply(classify)

output_file.parent.mkdir(parents=True, exist_ok=True)
customer_sales.to_csv(output_file, index=False)

print("Segmentation Done")