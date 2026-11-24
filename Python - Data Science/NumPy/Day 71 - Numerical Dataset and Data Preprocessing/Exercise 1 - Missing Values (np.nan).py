import numpy as np

marks = np.array([45 , 60 , np.nan , 80 ,np.nan, 95, 100 ,70])
print(marks)

missing_values = np.isnan(marks)
count_non_valid = np.sum(np.isnan(marks))



print(missing_values)
print("Non Valid Values :",count_non_valid)

print("="*50)
print("Original Dataset ")
print(marks)
# Clean the Data set
print("="*50)
print("Clean Marks :")

clean_marks = marks[~np.isnan(marks)]
print(clean_marks)
print("="*50)
print("Valid Values :",len(clean_marks))