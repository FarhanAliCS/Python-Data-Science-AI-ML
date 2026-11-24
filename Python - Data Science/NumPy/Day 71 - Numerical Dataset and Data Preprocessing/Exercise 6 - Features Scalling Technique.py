import numpy as np

data = np.array([
    [20 ,30000],
    [30 ,50000],
    [25 ,80000],
    [30 ,100000],
    [35 ,120000]
])

column_mean = np.mean(data , axis=0)
column_std = np.std(data , axis=0)
standardization = (data - column_mean)/column_std
print("Original Dataset : \n",data)
print("Mean of Original Dataset :",column_mean)
print("Standard Diviation :",column_std)
print("Standardized Dataset :\n", standardization)
print("Mean of standardized dataset :",np.mean(standardization , axis=0))
print("Standard Diviation of standardized Dataset :",np.std(standardization , axis=0))