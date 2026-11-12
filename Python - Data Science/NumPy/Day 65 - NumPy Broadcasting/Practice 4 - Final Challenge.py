import numpy as np

A = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

B = np.array([1, 2, 3])

C = np.array([
    [10],
    [20],
    [30]
])

addition = A + B
print("Addition :",addition)
print("Shape :",addition.shape)

subtraction = A - C
print("Subtraction of A - C :",subtraction)
print("Shape :",subtraction.shape)

multiplication = B * C
print("Multiplication B * C :",multiplication)
print("Shape :",multiplication.shape)


