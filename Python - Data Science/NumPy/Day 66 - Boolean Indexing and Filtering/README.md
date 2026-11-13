###   Day 66 — NumPy Boolean Indexing and Filtering

# Overview

Learned how to select, filter, count, classify, and sort NumPy array elements using Boolean conditions and built-in NumPy functions.

# Topics Covered

1. Boolean Arrays
2. Boolean Indexing
3. Filtering with Conditions
4. Multiple Conditions ("&", "|", "~")
5. "np.where()"
6. "np.unique()"
7. "return_counts=True"
8. "np.sort()"
9. "np.argsort()"

# Important Functions

Function| Purpose
"np.where()"| Find indexes or select values based on conditions
"np.unique()"| Find unique elements
"np.unique(return_counts=True)"| Find unique elements and their frequencies
"np.max()"| Find maximum value
"np.argmax()"| Find index of maximum value
"np.sort()"| Sort array values
"np.argsort()"| Return indexes that sort an array
"np.sum()"| Calculate sum or count True values

# Boolean Operators

- "&" — AND
- "|" — OR
- "~" — NOT

Always use parentheses around individual conditions when combining NumPy Boolean expressions.

Practical Project — Student Marks Analyzer

import numpy as np

marks = np.array([45, 67, 89, 32, 76, 95, 50, 84, 67, 90])

passed_students = marks[marks >= 50]
count_passed_students = len(passed_students)

values, frequencies = np.unique(marks, return_counts=True)

index = np.argmax(frequencies)

marks_descending_order = np.sort(marks)[::-1]

index_marks_greater_80 = np.where(marks > 80)

print("Student Marks Analyzer")
print("Passed students:", passed_students)
print("Count of passed students:", count_passed_students)
print("Marks and frequencies:", values, frequencies)
print("Most occurring mark:", values[index])
print("Descending order:", marks_descending_order)
print("Indexes of marks greater than 80:", index_marks_greater_80)

# Applications in Data Science and AI/ML

- Filtering datasets based on conditions.
- Identifying unique categories and values.
- Counting class frequencies.
- Sorting and ranking data.
- Finding positions of specific values.
- Preparing and analyzing datasets.

Day 66 Status

Completed

Next: Day 67 — NumPy Random Number Generation.