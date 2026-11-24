import numpy as np

marks = np.array([45 , 55, np.nan , 75 , 85 , np.nan , 95])

median = np.nanmedian(marks)
marks[np.isnan(marks)] = 0

print(marks)
