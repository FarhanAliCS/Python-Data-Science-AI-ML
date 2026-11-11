   ### Day 64 — NumPy Array Manipulation

# Overview

Today, I learned how to manipulate NumPy arrays by changing their shapes, combining arrays, splitting arrays, and resizing them.

These operations are important in Data Science, Machine Learning, and AI because datasets often need to be transformed into different shapes before analysis or model training.

# Topics Covered

# 1. reshape()

Changes the shape of an array without changing its total number of elements.

import numpy as np

numbers = np.array([1, 2, 3, 4, 5, 6])

print(numbers.reshape(2, 3))
print(numbers.reshape(3, 2))

Important: The total number of elements must remain the same.

Using "-1", NumPy automatically calculates the dimension.

numbers.reshape(2, -1)

# 2. flatten()

Converts a multidimensional array into a one-dimensional array and always returns a copy.

data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

result = data.flatten()

# 3. ravel()

Converts a multidimensional array into a one-dimensional array.

result = data.ravel()

Difference:

- "flatten()" always returns a copy.
- "ravel()" returns a view when possible; otherwise, it returns a copy.

# 4. transpose() and .T

Transpose swaps the axes of an array. For a 2D matrix, rows become columns and columns become rows.

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix.transpose())
print(matrix.T)

Original shape: "(2, 3)"

Transposed shape: "(3, 2)"

# 5. concatenate()

Joins two or more arrays along an existing axis.

a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

result = np.concatenate((a, b))
print(result)

For 2D arrays:

np.concatenate((a, b), axis=0)  # Vertical joining
np.concatenate((a, b), axis=1)  # Horizontal joining

# 6. stack()

Joins arrays along a new axis.

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.stack((a, b), axis=0))
print(np.stack((a, b), axis=1))

Difference:

- "concatenate()" uses an existing axis.
- "stack()" creates a new axis.

# 7. vstack() and hstack()

vstack(): Stacks arrays vertically.

np.vstack((a, b))

hstack(): Stacks arrays horizontally.

np.hstack((a, b))

# 8. split()

Divides an array into equal-sized parts.

numbers = np.array([10, 20, 30, 40, 50, 60])

result = np.split(numbers, 3)

for arr in result:
    print(arr)

# 9. array_split()

Divides an array into a specified number of parts, even if the parts have unequal sizes.

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

result = np.array_split(numbers, 3)

for arr in result:
    print(arr)

Difference:

- "split()" requires equal-sized divisions.
- "array_split()" allows unequal-sized divisions.

# 10. resize()

Changes the shape and number of elements in an array.

numbers = np.array([1, 2, 3, 4])

result = np.resize(numbers, (3, 3))

print(result)

NumPy repeats elements when the new size is larger and removes extra elements when the new size is smaller.

Important: "np.resize()" returns a new array and does not modify the original array.

---

# Important Comparison Table

Function| Purpose
"reshape()"| Changes array shape
"flatten()"| Converts to 1D and returns a copy
"ravel()"| Converts to 1D and returns a view when possible
"transpose()"| Swaps axes
"concatenate()"| Joins along an existing axis
"stack()"| Joins along a new axis
"vstack()"| Vertical stacking
"hstack()"| Horizontal stacking
"split()"| Divides into equal parts
"array_split()"| Divides into potentially unequal parts
"resize()"| Changes shape and potentially element count

# Practical Exercises Completed

- Reshaped 1D arrays into 2D and 3D arrays.
- Used "-1" for automatic dimension calculation.
- Compared "flatten()" and "ravel()".
- Transposed matrices using ".transpose()" and ".T".
- Combined 1D and 2D arrays using "concatenate()".
- Practiced "axis=0" and "axis=1".
- Used "stack()", "vstack()", and "hstack()".
- Divided arrays using "split()" and "array_split()".
- Increased and decreased array sizes using "resize()".
- Completed a mixed practical challenge using student marks.

# AI/ML Applications

Array manipulation is useful in:

- Preparing datasets for machine learning.
- Changing the dimensions of input data.
- Transposing feature matrices.
- Combining datasets.
- Splitting datasets into smaller sections.
- Reshaping image data for neural networks.

# Day 64 Status

Completed Topics: NumPy Array Manipulation

Status: Completed

Next: Day 65 — NumPy Broadcasting

---

Learning Python for Data Science, Machine Learning, and AI — One Day at a Time.