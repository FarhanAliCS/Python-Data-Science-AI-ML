import numpy as np

data=np.array([1,2,3,4,5,6,7,8,9,10,11,12])

print(data.reshape((3,4))) # 3,4 Array Reshape
print(data.reshape((2,2,3))) # 3D Array 2 rows 2 colums and 3 Blocks
print(data.reshape((4,-1))) # 4 rows Automatically  calulating columns


