import numpy as np

marks = np.array([ 10,20,30,40,50,60,70,80,90,100])

print("25th Percentile :",np.percentile(marks , 25))
print("50th Percentile :",np.percentile(marks , 50))
print("75th Percentile :",np.percentile(marks , 75))
print("90th Percentile :",np.percentile(marks , 90))