# 🐼 Introduction to Pandas

# Day 73 | Python Data Science & AI/ML Roadmap

# 📌 Overview

This learning session introduces Pandas, one of the most important Python libraries for data manipulation and analysis.

Pandas makes it easier to work with structured datasets, organize information into rows and columns, perform statistical calculations, and analyze real-world data.

In this session, I learned the fundamentals of Pandas DataFrames, created a student dataset, explored its structure, selected columns, and performed basic data analysis.

# 🎯 Learning Objectives

- Understand the Pandas library and its applications.
- Create DataFrames using Python dictionaries.
- Display and explore structured datasets.
- Understand DataFrame rows, columns, and shape.
- Select single and multiple columns.
- Retrieve the first and last rows.
- Perform basic statistical calculations.
- Filter records using conditional expressions.
- Identify maximum and minimum values.

# 🛠️ Technologies Used

- Python — Programming language
- Pandas — Data manipulation and analysis
- VS Code — Development environment

# 📚 Topics Covered

1. Introduction to Pandas

Learned that Pandas is a Python library used for:

- Data manipulation and analysis.
- Reading CSV and Excel files.
- Handling missing values.
- Cleaning real-world datasets.
- Performing statistical calculations.

2. Creating a DataFrame

Created a student dataset using a Python dictionary and converted it into a Pandas DataFrame.

import pandas as pd

students = {
    "Name": ["Farhan Ali", "Asad Khan", "Ashraf Ali",
             "Aziz Khan", "Ihtisham Ahmed"],
    "Age": [21, 20, 22, 23, 19],
    "Marks": [89, 90, 87, 50, 58],
    "Semester": [5, 5, 5, 5, 5]
}

df = pd.DataFrame(students)
print(df)

3. Displaying DataFrame Information

Practiced displaying complete datasets and retrieving specific rows.

print(df)
print(df.head(2))
print(df.tail(2))
print(df.shape)

Important methods and attributes:

Method / Attribute| Purpose
"head()"| Displays first rows
"tail()"| Displays last rows
"shape"| Returns rows and columns
"ndim"| Returns number of dimensions
"size"| Returns total number of elements

4. Selecting Columns

Learned how to access individual columns and multiple columns.

Single column:

print(df["Name"])

Multiple columns:

print(df[["Name", "Marks"]])

5. Basic Statistical Analysis

Performed basic statistical calculations on the student marks dataset.

print(df["Marks"].mean())
print(df["Marks"].max())
print(df["Marks"].min())
print(df["Name"].size)

Method| Purpose
".mean()"| Calculates average
".max()"| Finds maximum value
".min()"| Finds minimum value
".size"| Returns number of elements

6. Finding Highest and Lowest Performing Students

Used index-based methods to identify students with the highest and lowest marks.

highest_index = df["Marks"].idxmax()
lowest_index = df["Marks"].idxmin()

print(df.loc[highest_index, "Name"])
print(df.loc[lowest_index, "Name"])

7. Conditional Filtering

Practiced filtering student records using Boolean conditions.

print(df[df["Marks"] > 80])

Also practiced:

- Finding students scoring above 80.
- Finding students scoring below 70.
- Calculating average age.

# 🧠 Key Learning Outcomes

After completing this session, I learned:

- Fundamentals of Pandas.
- Difference between NumPy and Pandas.
- Creating and understanding DataFrames.
- Selecting single and multiple columns.
- Retrieving specific rows.
- Understanding DataFrame shape and dimensions.
- Performing basic statistical operations.
- Finding maximum and minimum values.
- Filtering records using conditions.
- Analyzing structured student datasets.

# 📂 Project Structure

Day 73 - Introduction to Pandas/
│
├── introduction_to_pandas.py
│
└── README.md

▶️ How to Run

1. Install Pandas

pip install pandas

2. Import Pandas

import pandas as pd

3. Run the Python file

python introduction_to_pandas.py

🎯 Project Status

# Completed — Day 73 ✅

This session marks the beginning of my Pandas learning journey in Phase 3 — Python Data Science, as part of my goal to become an AI/ML Engineer.

👨‍💻 Author

Farhan Ali

BS Computer Science Student | Aspiring AI/ML Engineer

- GitHub: "FarhanAliCS" (https://github.com/FarhanAliCS)

---

⭐ Learning Python, Data Science, and AI/ML — one step at a time.