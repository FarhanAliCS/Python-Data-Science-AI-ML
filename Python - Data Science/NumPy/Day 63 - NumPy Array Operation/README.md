  ### Day 63 — NumPy Array Operations

# Overview

Today I learned how to perform mathematical operations on NumPy arrays and how to analyze numerical data using comparison and statistical functions.

###     Topics Covered

# 1. Arithmetic Operations

Learned how to perform element-wise arithmetic operations:

- Addition ("+")
- Subtraction ("-")
- Multiplication ("*")
- Division ("/")
- Scalar operations

# 2. Vectorization

Learned how NumPy performs operations on entire arrays without manually iterating through every element.

Example:

import numpy as np

numbers = np.array([10, 20, 30])

print(numbers * 2)
# [20 40 60]

# 3. Comparison Operations

Learned how to compare array elements using:

- Greater than (">")
- Less than ("<")
- Greater than or equal (">=")
- Less than or equal ("<=")
- Equal ("==")
- Not equal ("!=")

These operations return Boolean arrays containing "True" and "False".

# 4. Aggregate Functions

Learned important NumPy functions for numerical analysis:

Function| Purpose
"np.sum()"| Calculates total
"np.min()"| Finds minimum value
"np.max()"| Finds maximum value
"np.mean()"| Calculates average
"np.average()"| Calculates weighted or ordinary average
"np.std()"| Calculates standard deviation
"np.var()"| Calculates variance

# 5. Variance and Standard Deviation

Variance: Measures the average squared distance of values from their mean.

Standard Deviation: Measures the spread of values around the mean in the original units.

Important points:

- Low standard deviation means values are closer to the mean.
- High standard deviation means values are more spread out.
- Zero standard deviation means all values are identical.
- Standard deviation is the square root of variance.

# 6. Population and Sample Statistics

Learned the difference between population and sample variance.

numbers = np.array([2, 4, 6, 8, 10])

# Population
print(np.var(numbers))
print(np.std(numbers))

# Sample
print(np.var(numbers, ddof=1))
print(np.std(numbers, ddof=1))

NumPy uses "ddof=0" by default for population calculations. "ddof=1" calculates sample statistics.

# Practical Exercises Completed

- Performed addition, subtraction, multiplication and division on arrays.
- Applied scalar operations.
- Compared numerical values using Boolean conditions.
- Identified passing and failing students using marks.
- Calculated total, minimum, maximum and average marks.
- Calculated variance and standard deviation.
- Compared two datasets with the same mean but different spreads.
- Analyzed a dataset with zero variance and zero standard deviation.

# Key Learning

I learned how NumPy makes numerical calculations easier and faster through vectorized operations and built-in statistical functions.

These concepts are important foundations for data analysis, statistics and machine learning.

Next Day

Day 64 — NumPy Array Manipulation