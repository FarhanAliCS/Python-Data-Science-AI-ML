import numpy as np

# generate a single random number 
single_number = np.random.rand()
print("Single Number :",single_number) 

# Generate 5 random numbers
numbers = np.random.rand(5)
print("5 Random Numbers :",numbers)

# 2D array with (3,2)
two_D_array = np.random.rand(3,2)
print("2D array .\n",two_D_array)

print(two_D_array.shape)

# It generate random  floating numbers betweeen 0 and 1