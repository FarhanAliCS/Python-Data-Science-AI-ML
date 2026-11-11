# array_split function use for unequal size 
#It does not divide each array into same size

import numpy as np

numbers = np.array([1,2,3,4,5,6,7,8,9,10])

result=np.array_split(numbers , 3)

for arr in result:
    print(arr)
    print(arr.shape)