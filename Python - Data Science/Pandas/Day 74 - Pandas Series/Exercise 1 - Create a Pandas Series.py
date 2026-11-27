import pandas as pd

marks = [89,78,48,59,69,70]

series = pd.Series(marks)
print("---: Marks Series :---")
print(series)
print("Indexes   :",series.index)
print("Shape     :",series.shape)
print("Date Type :",series.dtype)
print("Size      :",series.size)