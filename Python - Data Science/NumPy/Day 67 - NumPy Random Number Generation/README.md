###   Day 67 – NumPy Random Number Generation

# Overview

Completed Day 67 of my Python Data Science and AI/ML roadmap.

Today, I learned how to generate random numbers, work with different probability distributions, control randomness using seeds, perform random sampling, and generate synthetic datasets using NumPy.

# Topics Covered

1. Random Number Generation

- Introduction to random numbers.
- Applications in Data Science and Machine Learning.

2. Uniform Random Numbers

- "np.random.rand()"
- Generate single random numbers.
- Generate 1D and 2D random arrays.

3. Random Integers

- "np.random.randint()"
- Generate random integers within a range.
- Generate random integer matrices.

4. Standard Normal Distribution

- "np.random.randn()"
- Mean = 0.
- Standard deviation = 1.
- Understanding positive and negative values.

5. Custom Normal Distribution

- "np.random.normal()"
- "loc" represents mean.
- "scale" represents standard deviation.
- "size" specifies the output shape.

6. Random Seed

- "np.random.seed()"
- Reproducibility of random results.
- Comparing arrays using "np.array_equal()".

7. Random Sampling

- "np.random.choice()"
- Random selection of elements.
- Sampling with and without replacement.

8. Shuffling and Permutation

- "np.random.shuffle()"
- "np.random.permutation()"
- Difference between modifying the original array and returning a new array.

9. Synthetic Dataset Generation

- "np.random.uniform()"
- "np.column_stack()"
- Generating student study hours, attendance, and marks.
- Calculating average marks.
- Boolean indexing and filtering.

# Practical Project: Student Dataset Generation

# Generated a synthetic dataset for 10 students containing:

- Study hours
- Attendance percentage
- Exam marks

# Performed:

- Dataset creation.
- Shape inspection.
- Average marks calculation.
- Filtering students scoring 50 or above.

# Expected dataset shape: "(10, 3)".

# Key Learning Outcomes

- Generate random integers and floating-point numbers.
- Understand uniform and normal distributions.
- Reproduce random results using seeds.
- Perform random sampling and shuffling.
- Generate synthetic datasets for ML practice.
- Apply NumPy operations to basic data analysis.

# Technologies

- Python
- NumPy
- VS Code

Status

Day 67 Completed ✅

Next: Day 68 – NumPy Linear Algebra Fundamentals.