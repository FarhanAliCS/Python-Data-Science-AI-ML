import pandas as pd

series = pd.Series(
    [78 , 85 ,92 ,65 ,88 ,95],
    index = ["Ali","Ahmed","Sara","Usman","Ayesha","Bilal"]
)

print("-------: Statistical Analysis :-------")
print("Average      :",series.mean())
print("Median       :",series.median())
print("Maximum      :",series.max())
print("Minimum      :",series.min())
print("Sum of Makrs :",series.sum())