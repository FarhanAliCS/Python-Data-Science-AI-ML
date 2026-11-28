import pandas as pd
from pathlib import Path

current_file = Path(__file__).parent

csv_file = current_file / "students.csv"
excel_file = current_file / "students.xlsx"

# Read CSV
df = pd.read_csv(csv_file)

# Export DataFrame to Excel
df.to_excel(excel_file, index=False)

# Read Excel file
excel_df = pd.read_excel(excel_file)

print("======== First Five Rows ========")
print(excel_df.head())

print("\n======== Information ========")
excel_df.info()
