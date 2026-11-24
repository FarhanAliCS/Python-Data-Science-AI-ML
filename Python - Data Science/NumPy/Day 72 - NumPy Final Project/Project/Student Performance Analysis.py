import numpy as np


# ============================================================
#              STUDENT PERFORMANCE ANALYSIS
#                    NumPy Data Analysis
# ============================================================


# ============================================================
#                     1. DATASET
# ============================================================

students = np.array([
    "Ali", "Ahmed", "Sara", "Usman", "Ayesha",
    "Bilal", "Fatima", "Hamza", "Zain", "Hina"
])

marks = np.array([
    [85, 78, 90, 88, 92],
    [70, 65, 75, 80, 72],
    [95, 92, 98, 96, 94],
    [60, 55, 65, 70, 62],
    [88, 90, 85, 92, 89],
    [45, 50, 48, 55, 52],
    [92, 95, 90, 94, 96],
    [75, 80, 78, 82, 79],
    [55, 60, 58, 62, 57],
    [80, 85, 82, 88, 84]
])

subjects = np.array([
    "Python",
    "Mathematics",
    "Statistics",
    "Computer Science",
    "Database"
])


# ============================================================
#                    2. DATASET INFORMATION
# ============================================================

print("\n" + "=" * 60)
print("                  DATASET INFORMATION")
print("=" * 60)

print("\n------ Student Dataset ------")

print(students)
print("Shape              :", students.shape)
print("Dimension          :", students.ndim)
print("Number of Students :", marks.shape[0])

print("\n------ Marks Dataset ------")

print(marks)
print("Shape              :", marks.shape)
print("Dimension          :", marks.ndim)
print("Number of Subjects :", marks.shape[1])


# ============================================================
#                 3. SUBJECT STATISTICAL ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("             SUBJECT STATISTICAL ANALYSIS")
print("=" * 60)

average_marks = np.mean(marks, axis=0)

for i in range(len(average_marks)):
    print(
        f"Subject {i+1}: {subjects[i]} "
        f": Average : {average_marks[i]}"
    )


print("\n------ Subject With Highest Average ------")

highest_average = np.argmax(average_marks)

print(
    f"Subject : {subjects[highest_average]} "
    f": Average : {average_marks[highest_average]}"
)


print("\n------ Subject With Lowest Average ------")

lowest_average = np.argmin(average_marks)

print(
    f"Subject : {subjects[lowest_average]} "
    f": Average : {average_marks[lowest_average]}"
)


# ============================================================
#                 4. STUDENT PERFORMANCE ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("              STUDENT PERFORMANCE ANALYSIS")
print("=" * 60)

print("\n------ Each Student Average Marks ------")

average = np.mean(marks, axis=1)

for i in range(len(average)):
    print(f"{i+1}. {students[i]} : {average[i]}")


print("\n------ Highest Performing Student ------")

greater_average = np.argmax(average)

print(
    f"Name : {students[greater_average]} "
    f": Average : {average[greater_average]}"
)


print("\n------ Lowest Performing Student ------")

lower = np.argmin(average)

print(
    f"Name : {students[lower]} "
    f": Average : {average[lower]}"
)


# ============================================================
#                     5. TOP 3 STUDENTS
# ============================================================

print("\n" + "=" * 60)
print("                    TOP 3 STUDENTS")
print("=" * 60)

total = np.sum(marks, axis=1)

print("Total Marks:", total)

top_students = np.argsort(total)[::-1]

print("Sorted Indices:", top_students)

count = 0

print("\nTop Performing Students:")

for i in top_students[:3]:
    count += 1

    print(
        f"Position {count} : {students[i]} "
        f": Total Marks : {total[i]}"
    )


# ============================================================
#                    6. PASS AND FAIL ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("                 PASS AND FAIL ANALYSIS")
print("=" * 60)

passed_students = np.all(marks >= 50, axis=1)

failed_students = np.any(marks < 50, axis=1)

count_passed = np.sum(passed_students)

count_failed = np.sum(failed_students)


print("\n------ Passed Students ------")

print(students[passed_students])


print("\n------ Failed Students ------")

print(students[failed_students])


print("\nCount of Passed Students :", count_passed)

print("Count of Failed Students :", count_failed)


# ============================================================
#               7. MAXIMUM AND MINIMUM ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("              MAXIMUM AND MINIMUM ANALYSIS")
print("=" * 60)

maximum_marks = np.max(marks, axis=0)

minimum_marks = np.min(marks, axis=0)


for i in range(len(maximum_marks)):

    print(
        f"Subject {i+1} : "
        f"Highest Marks : {maximum_marks[i]} "
        f": Lowest Marks : {minimum_marks[i]}"
    )


students_highest = np.argmax(marks, axis=0)

print("\n------ Students With Highest Marks in Each Subject ------")

for i in range(len(subjects)):

    print(
        f"{subjects[i]} : "
        f"{students[students_highest[i]]} "
        f": {maximum_marks[i]}"
    )


# ============================================================
#                  8. STANDARD DEVIATION ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("               STANDARD DEVIATION ANALYSIS")
print("=" * 60)

std_subject = np.std(marks, axis=0)

highest_std = np.argmax(std_subject)

count = 0

for std in std_subject:

    count += 1

    print(
        f"Subject : {count} "
        f": Standard Deviation : {std}"
    )


print(
    "\nHighest Standard Deviation :",
    std_subject[highest_std],
    "Subject",
    highest_std + 1
)


# ============================================================
#                  9. MIN-MAX NORMALIZATION
# ============================================================

print("\n" + "=" * 60)
print("                  MIN-MAX NORMALIZATION")
print("=" * 60)

minimum = np.min(marks, axis=0, keepdims=True)

maximum = np.max(marks, axis=0, keepdims=True)

normalization = (marks - minimum) / (maximum - minimum)

print("\n------ Normalized Form For Each Student ------\n")

print(normalization)


# ============================================================
#                    10. STANDARDIZATION
# ============================================================

print("\n" + "=" * 60)
print("                     STANDARDIZATION")
print("=" * 60)

mean = np.mean(marks, axis=0, keepdims=True)

std = np.std(marks, axis=0, keepdims=True)

standardization = (marks - mean) / std


print("\n------ Standardized Form For Each Student ------")

print(standardization)


print("\nMean of Standardized Data:")

print(np.mean(standardization, axis=0))


print("\nStandard Deviation of Standardized Data:")

print(np.std(standardization, axis=0))


# ============================================================
#                   11. FINAL ACADEMIC REPORT
# ============================================================

print("\n" + "=" * 60)
print("                  FINAL ACADEMIC REPORT")
print("=" * 60)

print("Total Students              :", students.size)

print("Total Subjects              :", subjects.size)

print("Overall Class Average       :", np.mean(marks))

print("Highest Performing Student  :", students[np.argmax(total)])

print("Lowest Performing Student   :", students[np.argmin(total)])

print("Best Performing Subject     :", subjects[np.argmax(average_marks)])

print("Worst Performing Subject    :", subjects[np.argmin(average_marks)])

print("Passed Students             :", students[passed_students])

print("Failed Students              :", students[failed_students])

print("=" * 60)

print("             END OF STUDENT ANALYSIS REPORT")

print("=" * 60)