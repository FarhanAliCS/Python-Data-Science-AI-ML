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

print("\nShape :",df.shape)
print("Dimenion :",df.ndim)
print("Size      :",df.size)

print("\nColumn Names :",df.columns)
print("\nIndexes      :",df.index)

print("\n-------: DataType :---------     :",)
print(df.dtypes)

