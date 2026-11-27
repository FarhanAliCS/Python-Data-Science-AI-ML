import pandas as pd

series = pd.Series(
    [78 , 85 ,92 ,65 ,88 ,95],
    index = ["Ali","Ahmed","Sara","Usman","Ayesha","Bilal"]
)

print("--------: Indexing :---------")

print("Sara Marks  :",series.loc["Sara"])

print("Ahmed Marks :",series.iloc[1])

print("-----: First Three Students :------")
print(series.head(3))
print("------: Last 2 Students :------")
print(series.tail(2))
