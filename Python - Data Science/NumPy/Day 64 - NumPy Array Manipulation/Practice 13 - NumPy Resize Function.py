import numpy as np

# Increaseing Size

numbers = np.array([1,2,3,4])

result=np.resize(numbers , (3,3))

print(result)
print(result.shape)

# Decreasing Size

numbers = np.array([10,20,30,40,50,60])

result = np.resize(numbers , (2,2))

print(result)
print(result.shape)