import pandas as pd
from pathlib import Path

# Get the current folder
current_file = Path(__file__).parent

# Define input file paths
excel_file = current_file / "students.xlsx"
csv_file = current_file / "students.csv"

# Read Excel and CSV files
df = pd.read_excel(excel_file)
df2 = pd.read_csv(csv_file)


# ==========================================
#           Export Data to Files
# ==========================================

# Export DataFrame to Excel
excel_file1 = current_file / "students_output.xlsx"
df.to_excel(excel_file1, index=False)

# Export DataFrame to CSV
csv_file1 = current_file / "students_output.csv"
df2.to_csv(csv_file1, index=False)


# ==========================================
#          Read Exported Files
# ==========================================

csv_df = pd.read_csv(csv_file1)
excel_df = pd.read_excel(excel_file1)


# ==========================================
#             Display CSV Data
# ==========================================

print("\n" + "=" * 50)
print("                CSV File Data")
print("=" * 50)
print(csv_df)


# ==========================================
#            Display Excel Data
# ==========================================

print("\n" + "=" * 50)
print("               Excel File Data")
print("=" * 50)
print(excel_df)