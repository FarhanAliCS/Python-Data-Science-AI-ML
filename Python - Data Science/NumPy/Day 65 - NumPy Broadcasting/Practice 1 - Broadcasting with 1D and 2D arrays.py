import numpy as np

matrix = np.array([
    [10,20,30],
    [40,50,60]
])

numbers = np.array([1,2,3])

print("Original Array Shape :",matrix.shape )
print("Original 1D array Shape :",numbers.shape)

# Multiplication
 
result1 = matrix * numbers
print(result1)
print(result1.shape)

#Subtraction

result2=matrix - numbers
print(result2)
print(result2.shape)