import numpy as np

prices = np.array([100,200,300,400,500])

minimum = np.min(prices)
maximum = np.max(prices)

normalization = (prices - minimum)/(maximum - minimum)

print("Minimum Value :",minimum)
print("Maximum value :",maximum)
print("Original Dataset : ",prices)
print("Normalized Dataset :",normalization)

