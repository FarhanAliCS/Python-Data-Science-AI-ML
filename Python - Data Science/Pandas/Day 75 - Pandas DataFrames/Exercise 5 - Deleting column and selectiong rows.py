import pandas as pd

students = {
    "Name": ["Ali", "Ahmed", "Sara", "Usman", "Ayesha", "Bilal"],
    "Age": [20, 21, 19, 22, 20, 23],
    "Marks": [85, 90, 95, 70, 88, 55],
    "Semester": [3, 4, 3, 5, 4, 6],
    "Department": [
        "CS", "SE", "CS", "IT", "CS", "SE"
    ],
    "Bonus":[90,95,100,75,93,60]
}

#=================================================

#Create a DataFrame
df = pd.DataFrame(students)
print("=" * 50)
print("          Students DataFrame")
print("=" * 50)
print(df)

#=================================================

df = df.drop("Bonus" , axis=1)
print("\n"+"=" * 50)
print("        Update DataFrame")
print("=" * 50)
print(df)

#=================================================

print("\n"+"=" * 50)
print("         First Row")
print("=" * 50)
print(df.loc[0])

#=================================================

print("\n"+"=" * 50)
print("       Third Student")
print("=" * 50)
print(df.iloc[2])

#=================================================

print("\n"+"=" * 50)
print("        Name of Student at index 2")
print("=" * 50)
print(df.loc[2,"Name"])

#=================================================

print("\n"+"=" * 50)
print("        First Three Rows and 2 Column")
print("=" * 50)
print(df.iloc[:3,:2])

#=================================================
# axes 1 mean all column in first row