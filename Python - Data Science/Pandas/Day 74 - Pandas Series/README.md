# ## Day 74 — Pandas Series

# Overview

Today, I learned about Pandas Series, a one-dimensional labeled data structure in Python. I practiced creating Series from lists and dictionaries, using custom indexes, accessing values, performing mathematical operations, calculating statistics, and filtering data with conditions.

# Learning Objectives

- Understand what a Pandas Series is.
- Create Series from Python lists and dictionaries.
- Use default and custom indexes.
- Understand Series attributes.
- Access elements using "loc[]" and "iloc[]".
- Perform mathematical operations.
- Apply statistical methods.
- Filter data using Boolean conditions.

# Topics Covered

1. Creating a Series

import pandas as pd

marks = [85, 90, 75, 95, 60]
series = pd.Series(marks)

print(series)

2. Series Attributes

print(series.index)
print(series.values)
print(series.dtype)
print(series.shape)
print(series.size)

3. Custom Index

students = ["Ali", "Ahmed", "Sara", "Usman", "Ayesha"]

series = pd.Series(
    [78, 85, 92, 65, 88],
    index=students
)

print(series)

4. Creating a Series from a Dictionary

students = {
    "Farhan": 89,
    "Ali": 88,
    "Ahmed": 90,
    "Afzal": 87
}

series = pd.Series(students)
print(series)

5. Accessing Elements

- "loc[]" — Access elements using index labels.
- "iloc[]" — Access elements using integer positions.

print(series.loc["Farhan"])
print(series.iloc[1])

6. Mathematical Operations

print(series + 5)
print(series - 5)
print(series * 2)
print(series / 2)

7. Statistical Operations

print(series.mean())
print(series.median())
print(series.max())
print(series.min())
print(series.sum())

8. Boolean Filtering

print(series[series > 80])
print(series[series < 70])

Practice Tasks Completed

- Created Series from lists.
- Created Series using custom indexes.
- Created Series from dictionaries.
- Accessed values using "loc[]" and "iloc[]".
- Used "head()" and "tail()".
- Calculated mean, median, maximum, minimum, and sum.
- Filtered values using Boolean conditions.
- Practiced filtering with multiple conditions using "&".

# Key Concepts Learned

Concept| Description
Series| One-dimensional labeled data structure
Index| Labels used to identify elements
"loc[]"| Label-based selection
"iloc[]"| Position-based selection
Boolean Filtering| Selecting values based on conditions
Statistics| Analyzing numerical data

Difference Between Series and DataFrame

Series| DataFrame
One-dimensional| Two-dimensional
Contains one axis of labels| Contains row and column labels
Similar to a single column| Similar to a complete table

# Repository Structure

Python - Data Science/
└── Pandas/
    └── Day 74 - Pandas Series/
        ├── pandas_series.py
        └── README.md

# Technologies Used

- Python
- Pandas
- VS Code

Progress

Status: Completed

Day: 74

Next: Day 75 — Pandas DataFrames

---

Part of my Python Data Science and AI/ML learning journey.