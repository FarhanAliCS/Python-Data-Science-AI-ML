import pandas as pd
students = {
    "Name": ["Ali", "Ahmed", "Sara", "Usman", "Ayesha", "Bilal"],
    "Age": [20, 21, 19, 22, 20, 23],
    "Marks": [85, 90, 95, 70, 88, 55],
    "Semester": [3, 4, 3, 5, 4, 6],
    "Department": [
        "CS", "SE", "CS", "IT", "CS", "SE"
    ]
}

#Create a DataFrame
df = pd.DataFrame(students)
print("=" * 55)
print("           Students DataFrame ")
print("=" * 55)
print(df)


# Add passed column where marks greater then or equal to 60
df["passed"] = df["Marks"] >= 60

# Add column called Bonus, containing 5 extra marks for every student.
df["Bonus"] = df["Marks"]+5

# Modify the age column by adding 1 to every student's age.
df["Age"]=df["Age"]+1

print("\n"+"=" * 65)
print("             Updated DataFrme")
print("=" * 65)
print(df)
print("=" * 65)