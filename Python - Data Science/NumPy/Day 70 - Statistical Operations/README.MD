###   Day 70 - NumPy Statistical Operations

# Overview

On Day 70, I learned NumPy statistical operations used to analyze datasets, understand data distributions, measure variation, and prepare data for Data Science and Machine Learning.

# Topics Covered

1. Mean

- Learned how to calculate the average of a dataset.
- Used "np.mean()" and ".mean()".

2. Median

- Learned how to find the middle value of sorted data.
- Understood the difference between mean and median.
- Used "np.median()".

3. Mode

- Learned how to identify the most frequent value.
- Used:
  - "np.unique()"
  - "return_counts=True"
  - "np.argmax()"
- Learned about bimodal datasets (datasets with two modes).

4. Percentiles and Quartiles

- Understood percentiles and how they describe data distribution.
- Learned the three main quartiles:
  - Q1: 25th percentile
  - Q2: 50th percentile (Median)
  - Q3: 75th percentile
- Used "np.percentile()".

5. Minimum and Maximum

- Learned how to find the smallest and largest values.
- Used "np.min()" and "np.max()".

6. Range

- Learned how to measure the difference between maximum and minimum values.

Formula:

"Range = Maximum - Minimum"

7. Variance and Standard Deviation

- Revised variance and standard deviation.
- Understood how they measure data spread around the mean.
- Learned the difference between low and high standard deviation.
- Used "np.var()" and "np.std()".

# Practical Exercise

Performed statistical analysis on a student marks dataset:

import numpy as np

marks = np.array([45, 60, 70, 70, 80, 90, 95, 100, 60, 85])

print("Mean:", np.mean(marks))
print("Median:", np.median(marks))

value, frequency = np.unique(marks, return_counts=True)
modes = value[frequency == frequency.max()]
print("Mode:", modes)

print("Q1:", np.percentile(marks, 25))
print("Q3:", np.percentile(marks, 75))

print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))

data_range = np.max(marks) - np.min(marks)
print("Range:", data_range)

print("Variance:", np.var(marks))
print("Standard Deviation:", np.std(marks))

# Important NumPy Functions

Function| Purpose
"np.mean()"| Calculate mean
"np.median()"| Calculate median
"np.unique()"| Find unique values
"np.argmax()"| Find index of maximum value
"np.percentile()"| Calculate percentiles
"np.min()"| Find minimum
"np.max()"| Find maximum
"np.var()"| Calculate variance
"np.std()"| Calculate standard deviation

# Learning Outcomes

After completing Day 70, I can:

- Calculate mean, median, and mode.
- Understand percentiles and quartiles.
- Calculate Q1, Q2, and Q3.
- Find minimum, maximum, and range.
- Understand variance and standard deviation.
- Analyze statistical properties of numerical datasets.
- Apply NumPy statistical functions to student performance data.

# Technologies Used

- Python
- NumPy
- VS Code

Status

Completed - Day 70

Next: Day 71 - NumPy Numerical Datasets and Data Preprocessing.