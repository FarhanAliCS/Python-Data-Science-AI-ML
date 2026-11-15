# np.random.randint() generate random int between a range provided
import numpy as np

# Generate 1 random int between 1 - 100
number = np.random.randint(1,100,size=1) 
print("1 Random int :",number)

#Generate 10 int between 1 - 50 
numbers = np.random.randint(1,50,size=10)
print("10 Random int :",numbers)

#Generate 3x3 matrix containing random int between 10,99
matrix = np.random.randint(10,99,size=(3,3))
print(matrix)

print("Minimum value :",matrix.min())
print("Maximum value :",matrix.max())
