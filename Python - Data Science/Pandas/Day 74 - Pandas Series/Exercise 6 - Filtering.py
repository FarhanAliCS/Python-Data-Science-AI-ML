import pandas as pd

series = pd.Series(
    [78 , 85 ,92 ,65 ,88 ,95],
    index = ["Ali","Ahmed","Sara","Usman","Ayesha","Bilal"]
)

print("-------: Student Marks > 80 :--------")
print(series[series > 80])
print("----------: Student Marks < 70 :---------")
print(series[series < 70])
print("------- : Student Score between 80 and 90 (inclusive) : ---------")
print(series[(series >= 80) & (series <= 90)])

