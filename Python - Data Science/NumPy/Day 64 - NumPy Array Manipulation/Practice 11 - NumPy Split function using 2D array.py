import numpy as np

matrix = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])

result= np.split(matrix , 2 , axis=1)

for arr in result:
    print(arr)
    print(arr.shape)