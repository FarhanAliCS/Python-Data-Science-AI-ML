###   🎓 Student Performance and Statistical Analysis System

# # # Day 72 — NumPy Final Project | Python Data Science & AI/ML Roadmap

## 📌 Project Overview

The Student Performance and Statistical Analysis System is a Python-based data analysis project developed using NumPy.

The project analyzes students' academic performance across five subjects using numerical computing and statistical techniques. It calculates subject averages, student rankings, pass/fail results, maximum and minimum marks, standard deviation, normalization, and standardization.

This project combines the NumPy concepts learned throughout the NumPy learning stage into one practical academic analysis system.

## 🎯 Project Objectives

- Analyze a student marks dataset using NumPy.
- Calculate subject-wise and student-wise averages.
- Identify the top-performing and lowest-performing students.
- Perform pass/fail analysis using Boolean indexing.
- Find maximum and minimum marks in each subject.
- Measure data variation using standard deviation.
- Apply Min-Max normalization and standardization.
- Generate a final academic performance report.

## 🛠️ Technologies Used

- Python — Programming language
- NumPy — Numerical computing and data analysis
- VS Code — Development environment

## 📂 Project Structure

Day 72 - NumPy Final Project/
│
├── student_performance_analysis.py
│
└── README.md

## 📊 Dataset Information

The project uses a sample dataset containing 10 students and their marks in five subjects.

# Students:

- Ali
- Ahmed
- Sara
- Usman
- Ayesha
- Bilal
- Fatima
- Hamza
- Zain
- Hina

# Subjects:

- Python
- Mathematics
- Statistics
- Computer Science
- Database

The marks are stored in a two-dimensional NumPy array, where each row represents a student and each column represents a subject.

## 🚀 Project Tasks and Features

1. Dataset Information

- Display student and marks datasets.
- Identify array shapes and dimensions.
- Calculate the total number of students and subjects.

NumPy concepts: "shape", "ndim", "size"

2. Subject Statistical Analysis

- Calculate average marks for each subject.
- Identify the subject with the highest average.
- Identify the subject with the lowest average.

NumPy concepts: "np.mean()", "np.argmax()", "np.argmin()"

3. Student Performance Analysis

- Calculate each student's average marks.
- Identify the highest-performing student.
- Identify the lowest-performing student.

NumPy concepts: "np.mean()", "axis=1", "np.argmax()", "np.argmin()"

4. Top 3 Students

- Calculate total marks for each student.
- Sort students according to their total marks.
- Display the top three students.

NumPy concepts: "np.sum()", "np.argsort()", array indexing

5. Pass and Fail Analysis

- Identify students who passed all subjects.
- Identify students who failed at least one subject.
- Calculate the total number of passed and failed students.

Passing Criteria: A student must score at least 50 marks in every subject.

NumPy concepts: "np.all()", "np.any()", Boolean indexing

6. Maximum and Minimum Marks Analysis

- Find the highest marks in each subject.
- Find the lowest marks in each subject.
- Identify the students who achieved the highest marks in each subject.

NumPy concepts: "np.max()", "np.min()", "np.argmax()", "np.argmin()"

7. Standard Deviation Analysis

- Calculate standard deviation for every subject.
- Identify the subject with the highest standard deviation.
- Understand variation in students' marks.

NumPy concepts: "np.std()", "np.argmax()"

8. Min-Max Normalization

Transform marks into a range between 0 and 1 using:

[
X_{normalized} = \frac{X-X_{min}}{X_{max}-X_{min}}
]

Normalization is performed column-wise for each subject.

NumPy concepts: "np.min()", "np.max()", broadcasting, array arithmetic

9. Standardization

Transform marks using the mean and standard deviation:

[
Z = \frac{X-\mu}{\sigma}
]

The standardized data has approximately:

- Mean = 0
- Standard deviation = 1

NumPy concepts: "np.mean()", "np.std()", broadcasting

10. Final Academic Report

Generate a final report containing:

- Total number of students.
- Total number of subjects.
- Overall class average.
- Highest-performing student.
- Lowest-performing student.
- Best-performing subject.
- Lowest-performing subject.
- Passed students.
- Failed students.

📈 Expected Analysis Results

Performance Metric| Result
Total Students| 10
Total Subjects| 5
Overall Class Average| 76.12
Best Student| Sara
Lowest Student| Bilal
Best Subject| Database
Lowest Subject| Mathematics
Passed Students| 9
Failed Students| 1

Results are based on the sample dataset included in the Python program.

## 🧠 Key Learning Outcomes

Through this project, I practiced and strengthened my understanding of:

- Creating and managing NumPy arrays.
- Working with multidimensional datasets.
- Understanding rows, columns, shapes, and axes.
- Performing statistical calculations.
- Sorting and ranking numerical data.
- Applying Boolean indexing and filtering.
- Using logical operations with "np.all()" and "np.any()".
- Finding maximum and minimum values.
- Measuring data distribution using standard deviation.
- Applying normalization and standardization.
- Using broadcasting for column-wise calculations.
- Building a complete data analysis program.

## ▶️ How to Run the Project

1. Clone the repository

git clone https://github.com/FarhanAliCS/Python-Data-Science-AI-ML.git

2. Navigate to the project folder

cd "Python-Data-Science-AI-ML/Python - Data Science/NumPy/Day 72 - NumPy Final Project"

3. Install NumPy

pip install numpy

4. Run the Python program

python student_performance_analysis.py

🎯 Project Status

Completed ✅

This project marks the completion of my NumPy learning stage in Phase 3 — Python Data Science, as part of my journey toward becoming an AI/ML Engineer.

👨‍💻 Author

Farhan Ali

BS Computer Science Student | Aspiring AI/ML Engineer

- GitHub: "FarhanAliCS" (https://github.com/FarhanAliCS)

---

⭐ Learning Python, Data Science, and AI/ML — one step at a time.