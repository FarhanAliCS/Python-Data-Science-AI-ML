# Boolean array is array that give only Two values True Or False
import numpy as np

numbers = np.array([5,12,18,25,30,40])

number_greater_20 = numbers > 20
numbers_less_18 = numbers < 18
numbers_equal_25 = numbers == 25

print(number_greater_20 , number_greater_20.dtype)
print(numbers_less_18 , numbers_less_18.dtype)
print(numbers_equal_25 ,numbers_equal_25.dtype)