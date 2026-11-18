import numpy as np

marks = np.array([45,60,70,70,80,90,95,100,60,85])

print("Mean                :",np.mean(marks))
print("Median              :",np.median(marks))
value , frequency = np.unique(marks , return_counts=True)
mode = value[frequency == frequency.max()]
print("Mode                :",mode)

print("25th Percentile :Q1 :",np.percentile(marks , 25))
print("75th Percentile :Q3 :",np.percentile(marks , 75))
print("Minimum , Maximum   :",np.min(marks),np.max(marks))
range = np.max(marks) - np.min(marks)
print("Range :",range)
print("Variance            :",np.var(marks))
print("Standard Deviation  :",np.std(marks))
