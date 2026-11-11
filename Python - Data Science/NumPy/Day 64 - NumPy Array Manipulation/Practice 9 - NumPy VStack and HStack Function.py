import numpy as np

a = np.array([10,20,30])
b = np.array([40,50,60])

result1=np.vstack((a,b))
result2=np.hstack((a,b))

print(result1)
print(result1.shape)

print(result2)
print(result2.shape)

# V stack concatenate values vertically and H stack concatenate values horizontaly