import numpy as np

numbers = np.array([10,20,30,40,50,60])

# Select one random number from the array numbers
print(np.random.choice(numbers))

# Select 3 random numbers
print(np.random.choice(numbers , size=3))

#Select 3 unique numbers from the array
print(np.random.choice(numbers , size=3 , replace=False))

#Shuffle the original array
np.random.shuffle(numbers)
print("Original Array :",numbers)

# Permutation also shuffle but it does not change the original array instead it create a new array

new_array=np.random.permutation(numbers)
print(new_array)
print(numbers)
