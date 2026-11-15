import  numpy as np

number = np.random.rand(5)
print(number)

np.random.seed(42)
numbers=np.random.rand(5)
print(numbers)
np.random.seed(42)
numbers1=np.random.rand(5)
print(numbers1)
#Comparizion
print(np.array_equal(numbers , numbers1))
