import numpy as np

marks = np.array([35, 55, 72, 90, 42, 88, 60, 95])

print("Indexes of marks > 70 :",np.where(marks > 70))
print("Marks greater or equal to 50 = pass , less = Fail :",np.where(marks > 50 ,"Pass","Fail"))
print("Replace marks below then 50 with 0 :",np.where(marks < 50 , 0 , marks))