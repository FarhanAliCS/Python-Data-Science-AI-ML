import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

result=np.concatenate((a,b),axis=0)

result2 = np.concatenate((a,b),axis=1)

print(result)
print(result.shape)

print(result2)
print(result2.shape)

# Axis 0  mean concatenate these in rows and axis 0 mean concatenate in column

