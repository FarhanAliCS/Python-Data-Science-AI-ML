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

print("-------- : Students DataFrame : --------")
print(df)

print("\n---: Name Column :---")
print(df["Name"])

print("\n---: Name and Marks Column :---")
print(df[["Name","Marks"]])

print("\n---: Age , Semester , Department :---")
print(df[["Age","Semester","Department"]])

# One column return a series  because a one column is single dimention and series is a single dimention
