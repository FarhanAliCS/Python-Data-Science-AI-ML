import pandas as pd
from pathlib import Path

current_file = Path(__file__).parent
csv_file = current_file / "students.csv"


# Read Only First 4 Rows
print("\n"+"="*50)
print("           First 4 Rows using nrows")
print("="*50)
df = pd.read_csv(csv_file , nrows=4)
print(df)


print("\n"+"="*50)
print("           Name and Marks using usecols")
print("="*50)
df = pd.read_csv(csv_file , usecols=("Name","Marks"))
print(df)

print("\n"+"="*50)
print("           Set Name as the Index")
print("="*50)
df = pd.read_csv(csv_file , index_col="Name")
print(df)


