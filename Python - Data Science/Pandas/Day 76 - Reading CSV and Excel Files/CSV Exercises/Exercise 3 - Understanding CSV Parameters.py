import pandas as pd
from pathlib import Path

current_file = Path(__file__).parent
csv_file = current_file / "students.csv"
csv_file1=current_file / "students1.csv"

# Read csv file header = first row
print("\n"+"="*50)
print("         CSV Header is First Row")
print("="*50)
df = pd.read_csv(csv_file , header=0)
print(df)

print("\n"+"="*50)
print("         Skip Three Rows Excep Header")
print("="*50)
df = pd.read_csv(csv_file , skiprows=range(1,4))
print(df)

print("\n"+"="*50)
print("         Read csv File Separated by semicolon")
print("="*50)
df = pd.read_csv(csv_file1 , sep=";")
print(df)

print("\n"+"="*50)
print("         First 4 Rows")
print("="*50)
df = pd.read_csv(csv_file , nrows=4)
print(df)

print("\n"+"="*50)
print("        Select only Name column")
print("="*50)
df = pd.read_csv(csv_file , usecols=["Name"])
print(df)



