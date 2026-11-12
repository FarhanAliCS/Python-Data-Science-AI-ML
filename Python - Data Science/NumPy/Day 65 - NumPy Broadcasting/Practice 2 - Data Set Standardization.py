import numpy as np

data = np.array([
    [50,60],
    [60,70],
    [70,80],
    [80,90]
])

mean = np.mean(data , axis=0)
std= np.std(data , axis = 0)

standardizad_data= (data - mean)/std
print(standardizad_data)

print(mean.shape)
print(std.shape)
print(standardizad_data.shape)
standardized_mean = np.mean(standardizad_data, axis = 0)
print(standardized_mean)
