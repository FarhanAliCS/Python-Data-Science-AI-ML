import numpy as np
# np.random.randn() Generate numbers whose standard diviation is 1 and mean is 0

#Single Number
number=np.random.randn()
print(number)

# 10 random Numbers 
numbers=np.random.randn(10)
print(numbers)

#3,3 matrix
matrix=np.random.randn(3,3)
print(matrix)

print("mean :",matrix.mean())
print("Standard Diviation :",matrix.std())
