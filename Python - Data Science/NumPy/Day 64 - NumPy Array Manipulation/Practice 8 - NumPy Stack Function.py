import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

result=np.stack((a,b),axis= 0)
result2=np.stack((a,b),axis=1)


print(result)
print(result.shape)
print(result2)
print(result2.shape)

# Stack create new axis and concatenate use same exis to concatenate