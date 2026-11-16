### Project 1 — Student Performance Analytics

# 📌 Overview

This project is built using Python and NumPy to analyze student academic performance.

It generates a dataset containing marks for 20 students across 5 subjects and performs different statistical and analytical operations to understand student performance.

The project focuses on practical applications of NumPy, including array creation, aggregation, Boolean indexing, sorting, and statistical analysis.

# 🎯 Project Objectives

- Generate a student marks dataset using NumPy.
- Calculate total and average marks for each student.
- Calculate average marks for each subject.
- Identify students who passed all subjects.
- Find students with an average of 80 or above.
- Calculate the highest and lowest marks.
- Sort student marks in descending order.
- Find the most frequently occurring mark.
- Identify the top 3 students based on average marks.

# 📊 Dataset Information

Property| Value
Number of students| 20
Number of subjects| 5
Dataset shape| (20, 5)
Minimum marks| 0
Maximum marks| 100
Passing marks| 50
Random seed| 42

The dataset is generated using "np.random.randint()" and organized into a 2D NumPy array using "np.column_stack()".

# ⚙️ Features

1. Student Marks Generation

- Generates random marks for 20 students in 5 subjects.
- Creates a structured 2D NumPy array.

2. Student Performance Analysis

- Calculates total marks for each student.
- Calculates average marks for each student.
- Calculates average marks for each subject.

3. Pass Analysis

- Identifies students who passed all five subjects.
- Identifies students with an average of 80 or above.
- Uses Boolean indexing and "np.all()".

4. Marks Statistics

- Finds the highest and lowest marks.
- Sorts each student's marks in descending order.
- Finds unique marks and their frequencies using "np.unique()".
- Identifies the most frequently occurring mark using "np.argmax()".

5. Top 3 Students

- Uses "np.argsort()" to rank students according to their average marks.
- Displays the top three students with their marks and averages.

# 🧠 NumPy Concepts Practiced

NumPy Concept| Function / Method
Array creation| "np.array()"
Random number generation| "np.random.randint()"
Reproducibility| "np.random.seed()"
Combining arrays| "np.column_stack()"
Total marks| "np.sum()"
Average marks| "np.mean()"
All-subject pass check| "np.all()"
Maximum and minimum| ".max()", ".min()"
Sorting| "np.sort()"
Unique values and frequency| "np.unique()"
Highest frequency index| "np.argmax()"
Student ranking| "np.argsort()"
Boolean indexing| Conditional filtering

# 🛠️ Technologies Used

- Python
- NumPy
- Visual Studio Code


1. Open the project folder in VS Code.
2. Install NumPy if it is not already installed:

pip install numpy

4. Run the Python file:

python student_performance.py

# 📚 Learning Outcomes

Through this project, I practiced:

- Working with multidimensional NumPy arrays.
- Understanding "axis=0" and "axis=1".
- Performing vectorized calculations.
- Applying Boolean conditions to datasets.
- Calculating statistical values.
- Sorting and ranking data.
- Extracting useful information from numerical datasets.

✅ Project Status

Completed

This project is part of my Python Data Science and AI/ML learning roadmap.