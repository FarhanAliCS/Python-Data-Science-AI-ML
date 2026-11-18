import numpy as np

marks = np.array([50,60,70,70,80,90,70,60])

value , frequency = np.unique(marks , return_counts=True)
print("Unique Values :" ,value)
print("Frequencys    :",frequency)
print("Mode          :",value[np.argmax(frequency)])