import numpy as np

marks = np.array([40,50,60,70,80])

mean = np.mean(marks)
std = np.std(marks)

standardization = (marks - mean)/std

print("Mean :",mean)
print("Standard Diviation ",std)
print("Standardization :",standardization)
print(np.mean(standardization))