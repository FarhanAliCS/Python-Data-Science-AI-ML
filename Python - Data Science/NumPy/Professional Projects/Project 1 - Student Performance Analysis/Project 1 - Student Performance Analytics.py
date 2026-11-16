import numpy as np


# ============================================================
#                STUDENT MARKS DATA GENERATION
# ============================================================

np.random.seed(42)

# Generate marks for 20 students in 5 subjects
subject1 = np.random.randint(0, 101, size=20)
subject2 = np.random.randint(0, 101, size=20)
subject3 = np.random.randint(0, 101, size=20)
subject4 = np.random.randint(0, 101, size=20)
subject5 = np.random.randint(0, 101, size=20)

# Create the marks dataset
marks_dataset = np.column_stack((
    subject1,
    subject2,
    subject3,
    subject4,
    subject5
))


# ============================================================
#                  STUDENT PERFORMANCE ANALYSIS
# ============================================================

# Calculate total marks for each student
students_total_marks = np.sum(marks_dataset, axis=1)

# Calculate average marks for each student
average_marks = np.mean(marks_dataset, axis=1)

# Identify students who passed all subjects
student_passed = np.all(marks_dataset >= 50, axis=1)

# Identify students with an average of 80 or above
student_average = average_marks >= 80

# Calculate average marks for each subject
subject_average = np.mean(marks_dataset, axis=0)


# ============================================================
#                   MARKS STATISTICS
# ============================================================

# Find highest and lowest marks in the dataset
highest_marks = marks_dataset.max()
lowest_marks = marks_dataset.min()

# Sort each student's marks in descending order
reverse_sort_marks = np.sort(marks_dataset, axis=1)[:, ::-1]

# Calculate frequency of each unique mark
marks, frequency = np.unique(
    marks_dataset,
    return_counts=True
)

# Identify the mark with the highest frequency
highest_frequency = np.argmax(frequency)


# ============================================================
#                   DATASET INFORMATION
# ============================================================

print("\n" + "=" * 60)
print("              STUDENT PERFORMANCE ANALYTICS")
print("=" * 60)

print("\nMarks Dataset:\n", marks_dataset)

print("\nDataset Information:")
print("Shape      :", marks_dataset.shape)
print("Dimensions :", marks_dataset.ndim)
print("Data Type  :", marks_dataset.dtype)


# ============================================================
#                   STUDENT MARKS SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("                  STUDENT MARKS SUMMARY")
print("=" * 60)

print("\nTotal Marks of Each Student:")
print(students_total_marks)

print("\nAverage Marks of Each Student:")
print(average_marks)

print("\nAverage Marks of Each Subject:")
print(subject_average)


# ============================================================
#                    STUDENT PASS ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("                    PASS ANALYSIS")
print("=" * 60)

print("\nStudents Who Passed All Subjects:")
print(marks_dataset[student_passed])

print("\nStudents With Average Marks >= 80:")
print(marks_dataset[student_average])


# ============================================================
#                     MARKS STATISTICS
# ============================================================

print("\n" + "=" * 60)
print("                    MARKS STATISTICS")
print("=" * 60)

print("\nHighest Marks in Dataset:", highest_marks)

print("Lowest Marks in Dataset:", lowest_marks)

print("\nEach Student's Marks in Descending Order:")
print(reverse_sort_marks)

print("\nMost Frequently Occurring Mark:")
print(marks[highest_frequency])

print("Frequency:", frequency[highest_frequency])


# ============================================================
#                       TOP 3 STUDENTS
# ============================================================

print("\n" + "=" * 60)
print("                       TOP 3 STUDENTS")
print("=" * 60)

# Find indices of the top 3 students
top_student = np.argsort(average_marks)[::-1][:3]

for index in top_student:

    print(
        f"\nStudent {index + 1}: "
        f"Marks = {marks_dataset[index]}, "
        f"Average = {average_marks[index]:.2f}"
    )


# ============================================================
#                       END OF PROJECT
# ============================================================

print("\n" + "=" * 60)
print("          STUDENT PERFORMANCE ANALYSIS COMPLETED")
print("=" * 60)