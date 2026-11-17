import numpy as np

# equation1 = 3x + y =10 , eq2 = x + y = 6
A = np.array([
    [3 , 1],
    [1 , 1]
])
B = np.array([10 , 6])

print("x , y :",np.linalg.solve(A,B))


