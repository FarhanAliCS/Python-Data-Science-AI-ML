###   Day 65 — NumPy Broadcasting

# Overview

NumPy Broadcasting allows mathematical operations between arrays of different but compatible shapes without manually repeating or copying values.

# Topics Covered

1. Introduction to Broadcasting
2. Broadcasting with Scalars
3. Broadcasting with 1D and 2D Arrays
4. Broadcasting Rules
5. Compatible vs Incompatible Shapes
6. Broadcasting with 3D Arrays
7. Row and Column Broadcasting
8. Practical Machine Learning Example — Standardization

# Broadcasting Rules

Two dimensions are compatible when:

- Both dimensions are equal.
- One of the dimensions is 1.

Dimensions are compared from right to left. Missing leading dimensions are treated as 1.

# Examples

# Scalar Broadcasting

numbers = np.array([10, 20, 30])
result = numbers + 5

# 1D and 2D Broadcasting

matrix = np.array([[10, 20, 30],
                   [40, 50, 60]])

numbers = np.array([1, 2, 3])
result = matrix + numbers

# Row and Column Broadcasting

row = np.array([[5, 10, 15, 20]])

column = np.array([[2], [4], [6]])

result = row + column

Result shape: "(3, 4)"

# Machine Learning Application — Standardization

Standardization transforms numerical features to have approximately zero mean and unit standard deviation.

# Formula:

"z = (x - mean) / standard_deviation"

import numpy as np

data = np.array([
    [50, 60],
    [60, 70],
    [70, 80],
    [80, 90]
])

mean = np.mean(data, axis=0)
std = np.std(data, axis=0)

standardized_data = (data - mean) / std

print(standardized_data)
print(np.mean(standardized_data, axis=0))

# Important Concepts

- Broadcasting avoids manual repetition of array values.
- It supports efficient element-wise operations.
- Incompatible shapes produce a "ValueError".
- It is useful in feature scaling, normalization, and batch computations in Machine Learning.

Day 65 Status

Completed

Next: Day 66 — Boolean Indexing and Filtering.