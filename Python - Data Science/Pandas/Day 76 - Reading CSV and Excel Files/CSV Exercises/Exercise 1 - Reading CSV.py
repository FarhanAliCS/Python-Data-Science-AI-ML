import pandas as pd

from pathlib import Path

current_file = Path(__file__).parent

csv_file=current_file / "students.csv"

df = pd.read_csv(csv_file)

print("\n"+"="*45)
print("          Student DataFrame")
print("="*45)
print(df)
print("="*45)


# First Five Rows
print("\n"+"="*45)
print("          First Five Rows")
print("="*45)
print(df.head())
print("="*45)


# Last 3 Rows
print("\n"+"="*45)
print("          Last Three Rows")
print("="*45)
print(df.tail(3))
print("="*45)


# DataFrame Shape and Data Types
print("\nShape",df.shape)
print("-------: DataTyes :-------")
print(df.dtypes)