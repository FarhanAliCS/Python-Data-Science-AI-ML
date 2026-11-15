import numpy as np

# Geberate 10 random number with mean = 50 and SD = 10
numbers = np.random.normal(loc=50,scale=10,size=10)
print(numbers)

# Generate a 4x3 matrix with mean 100 and SD 15

matrix = np.random.normal(loc=100,scale=15,size=(4,3))
print(matrix)
print(matrix.mean())
print(matrix.std())
# mean = 100 and SD = 13
# Loc mean 100 and scale represent standard Diviation