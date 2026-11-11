import numpy as np
# Convert this 2D array into 1D using flatten().
# Print its shape.
# Change the first element of the flattened array to 999.
# Print the original array

data=np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

numbers=data.flatten()

print("Changed  Array :",numbers) # Changed Array 

numbers[0]=999 # Changed One element

print("Original Array : ",data) # Original Array 
print("Changed Array : ",numbers) # Changed Array
