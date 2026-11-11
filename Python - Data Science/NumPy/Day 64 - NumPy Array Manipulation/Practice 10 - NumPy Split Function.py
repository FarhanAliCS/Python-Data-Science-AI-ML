import numpy as np

numbers = np.array([10,20,30,40,50,60,70,80])

result = np.split(numbers , 4)

for arr in result:
    print(arr)
    print(arr.shape)