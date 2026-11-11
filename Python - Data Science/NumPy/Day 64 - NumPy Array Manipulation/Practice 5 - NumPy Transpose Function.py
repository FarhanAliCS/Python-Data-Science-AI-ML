import numpy as np

matrix=np.array([
    [10,20,30],
    [40,50,60]
])

result=matrix.transpose()
result2=matrix.T
print("Original :",matrix.shape)
print("Transpose :",result.shape)
print("Transpose using T :",result2.shape)

# The Rows beccome Column and Column become Rows