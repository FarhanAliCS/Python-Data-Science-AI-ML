import numpy as np

marks = np.array([70, 80, 70, 90, 80, 60, 90, 70])

print("All Unique Marks :",np.unique(marks))
values , counts = np.unique(marks , return_counts=True )
print("Unique marks and Count :",values, counts)
print("Count of unique marks :",len(np.unique(marks)))
values , counts = np.unique(marks , return_counts=True)

index=np.argmax(counts)
print("Maximum Count value :",values[index])


