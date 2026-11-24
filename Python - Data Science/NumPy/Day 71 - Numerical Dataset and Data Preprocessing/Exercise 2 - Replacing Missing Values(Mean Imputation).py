import numpy as np

marks = np.array([45 , 55, np.nan , 75 , 85 , np.nan , 95])

print("-----: Dataset :-----")
print(marks)
mean = np.nanmean(marks)
marks[np.isnan(marks)] = mean
print("Mean :",mean)
print("---: Dataset after Mean Imputation :---")
print(marks)
print("Mean after imputation :",np.mean(marks))