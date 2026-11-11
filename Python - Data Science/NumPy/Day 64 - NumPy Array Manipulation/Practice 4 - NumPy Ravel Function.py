import numpy as np

data=np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

numbers = data.ravel()

numbers[0] = 999

print("Original Array :",data)
print("Changed Array :",numbers)
# The Original Array changed becasue the ravel function offen change the original array to but the flatten function not
