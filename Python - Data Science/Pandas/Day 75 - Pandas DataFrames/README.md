 ### Day 75 — Pandas DataFrames

## Overview

Today, I learned about Pandas DataFrames, one of the most important data structures in Python Data Science.

A DataFrame is a two-dimensional, labeled data structure consisting of rows and columns. It is similar to an Excel spreadsheet or SQL database table.

I practiced creating DataFrames, inspecting datasets, selecting columns and rows, adding and modifying columns, deleting columns, and assigning values using conditional statements.

# Learning Objectives

- Understand Pandas DataFrames.
- Create DataFrames using dictionaries and NumPy arrays.
- Understand DataFrame attributes.
- Inspect datasets using Pandas methods.
- Select single and multiple columns.
- Add and modify DataFrame columns.
- Delete columns using "drop()".
- Select rows using "loc[]" and "iloc[]".
- Assign values using conditional statements.

# Topics Covered

1. Creating a DataFrame

import pandas as pd

students = {
    "Name": ["Ali", "Ahmed", "Sara", "Usman"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 90, 95, 70]
}

df = pd.DataFrame(students)

print(df)

2. Creating DataFrames from Different Sources

- Dictionary of lists
- List of dictionaries
- NumPy arrays

3. DataFrame Attributes

print(df.shape)
print(df.ndim)
print(df.size)
print(df.columns)
print(df.index)
print(df.dtypes)

Attribute| Description
"shape"| Returns rows and columns
"ndim"| Returns dimensions
"size"| Returns total elements
"columns"| Returns column names
"index"| Returns row indexes
"dtypes"| Returns data types of columns

4. Inspecting DataFrames

print(df.head())
print(df.head(3))

print(df.tail(2))

df.info()

print(df.describe())

- "head()" displays the first rows.
- "tail()" displays the last rows.
- "info()" provides dataset structure and information.
- "describe()" provides statistical summaries.

5. Selecting Columns

# Select one column
print(df["Name"])

# Select multiple columns
print(df[["Name", "Marks"]])

A single selected column returns a Series, while multiple selected columns return a DataFrame.

6. Adding and Modifying Columns

# Add a new column
df["Bonus"] = df["Marks"] + 5

# Modify an existing column
df["Age"] = df["Age"] + 1

# Conditional column
df["Passed"] = df["Marks"] >= 60

7. Conditional Assignment Using loc[]

df["Result"] = "Fail"

df.loc[df["Marks"] >= 60, "Result"] = "Pass"

8. Performance Classification

df["Performance"] = "Poor"

df.loc[df["Marks"] >= 90, "Performance"] = "Excellent"

df.loc[
    (df["Marks"] >= 80) & (df["Marks"] < 90),
    "Performance"
] = "Good"

df.loc[
    (df["Marks"] >= 60) & (df["Marks"] < 80),
    "Performance"
] = "Average"

9. Deleting Columns

df = df.drop("Bonus", axis=1)

- "axis=0" refers to the row axis.
- "axis=1" refers to the column axis.

10. Selecting Rows Using loc[] and iloc[]

# Label-based selection
print(df.loc[0])
print(df.loc[0, "Name"])

# Position-based selection
print(df.iloc[0])
print(df.iloc[2])

# Select multiple rows and columns
print(df.iloc[:3, :2])

# Practice Tasks Completed

- Created a student DataFrame.
- Inspected its shape, dimensions, size, indexes, and data types.
- Used "head()", "tail()", "info()", and "describe()".
- Selected individual and multiple columns.
- Added a Passed column using Boolean conditions.
- Added a Bonus column.
- Modified student ages.
- Deleted columns using "drop()".
- Selected rows using "loc[]" and "iloc[]".
- Created Result and Performance columns using conditional assignment.

# Important Concepts Learned

Concept| Description
DataFrame| Two-dimensional labeled data structure
Series| One-dimensional labeled data structure
"loc[]"| Label-based selection
"iloc[]"| Position-based selection
"axis=0"| Row axis
"axis=1"| Column axis
Boolean Filtering| Selecting data using conditions
Conditional Assignment| Assigning values based on conditions
Vectorization| Performing operations on entire columns

# Difference Between Series and DataFrame

Series| DataFrame
One-dimensional| Two-dimensional
Single axis| Two axes
Similar to one column| Similar to a complete table

# Repository Structure

Python - Data Science/
└── Pandas/
    └── Day 75 - Pandas DataFrames/
        ├── pandas_dataframe.py
        └── README.md

# Technologies Used

- Python
- Pandas
- NumPy
- VS Code

# Progress

Phase: Python Data Science

Section: Pandas

Day: 75

Status: Completed

Next: Day 76 — Reading CSV and Excel Files

---

Part of my journey toward becoming an AI/ML Engineer.