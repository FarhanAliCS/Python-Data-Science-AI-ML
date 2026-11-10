import numpy as np

class_a = np.array([50, 55, 60, 65, 70])
class_b = np.array([10, 35, 60, 85, 110])

print("Class A Mean :", np.mean(class_a))
print("Class B Mean :", np.mean(class_b))

print("Class A Variance :", np.var(class_a))
print("Class B Variance :", np.var(class_b))

print("Class A SD :",np.std(class_a))
print("Class B SD :",np.std(class_b))

# Class B is More Spread from the mean 
# Variance is the sprared diviation and Standard Diviation is the square root of variance 