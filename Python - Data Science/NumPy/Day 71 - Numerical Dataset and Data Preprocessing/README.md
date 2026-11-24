###   Day 71 - NumPy Numerical Datasets and Data Preprocessing

# Overview

On Day 71, I learned how to clean and preprocess numerical datasets using NumPy. I practiced handling missing values, replacing missing data, normalization, standardization, and feature scaling.

These techniques are important foundations for Data Science and Machine Learning.

## Topics Covered

1. Missing Values Detection

- Detect missing values using "np.isnan()".
- Count missing values using "np.sum()".
- Count valid values using Boolean indexing.

2. Removing Missing Values

- Remove NaN values using Boolean indexing.
- Understand how to create a clean dataset.

3. Mean Imputation

- Calculate the mean while ignoring NaN using "np.nanmean()".
- Replace missing values with the calculated mean.

4. Median Imputation

- Calculate median while ignoring missing values using "np.nanmedian()".
- Replace missing values with the median.
- Understand why median is more resistant to outliers than mean.

5. Min-Max Normalization

Normalization scales numerical values into a range, usually between 0 and 1.

Formula:

[
X_{normalized} = \frac{X-X_{min}}{X_{max}-X_{min}}
]

6. Standardization (Z-score Scaling)

Standardization transforms numerical data so that its mean becomes approximately 0 and its standard deviation becomes 1.

Formula:

[
Z = \frac{X-\mu}{\sigma}
]

7. Feature Scaling

- Understand why feature scaling is important in Machine Learning.
- Learn the difference between normalization and standardization.
- Understand its importance in KNN and K-Means algorithms.

## Practical Implementation

Standardization of a Numerical Dataset

import numpy as np

data = np.array([
    [20, 30000],
    [30, 50000],
    [25, 80000],
    [30, 100000],
    [35, 120000]
])

# Calculate column-wise mean and standard deviation
column_mean = np.mean(data, axis=0)
column_std = np.std(data, axis=0)

# Apply standardization
standardization = (data - column_mean) / column_std

print("Original Dataset:\n", data)
print("Mean:", column_mean)
print("Standard Deviation:", column_std)

print("Standardized Dataset:\n", standardization)

# Verify standardization
print("New Mean:", np.mean(standardization, axis=0))
print("New Standard Deviation:", np.std(standardization, axis=0))

Important NumPy Functions

Function| Purpose
"np.isnan()"| Detect missing values
"np.sum()"| Count missing values using Boolean masks
"np.nanmean()"| Calculate mean while ignoring NaN
"np.nanmedian()"| Calculate median while ignoring NaN
"np.min()"| Find minimum value
"np.max()"| Find maximum value
"np.mean()"| Calculate mean
"np.std()"| Calculate standard deviation

# Key Learnings

- Learned how to identify and handle missing numerical values.
- Practiced mean and median imputation.
- Understood the effect of outliers on mean and median.
- Learned Min-Max normalization.
- Learned Z-score standardization.
- Understood feature scaling and its importance in Machine Learning.
- Applied NumPy broadcasting for column-wise standardization.

# Technologies Used

- Python
- NumPy
- VS Code

Status

Day 71: Completed

Next: Continue learning NumPy and prepare for Pandas and Data Analysis.