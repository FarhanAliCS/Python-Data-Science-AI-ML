import numpy as np

a = np.array([10,20,30])
b = np.array([40,50,60])

result=np.concatenate((a,b),axis=0)

print(result)
print(result.shape)