import pandas as pd
students = {
    "Name": ["Ali", "Ahmed", "Sara", "Usman", "Ayesha", "Bilal"],
    "Age": [20, 21, 19, 22, 20, 23],
    "Marks": [85, 90, 95, 70, 88, 55],
    "Semester": [3, 4, 3, 5, 4, 6],
    "Department": [
        "CS", "SE", "CS", "IT", "CS", "SE"
    ]
}

#Create a DataFrame
df = pd.DataFrame(students)

print("-------- : Students DataFrame : --------")
print(df)

print("\n--------- : First Three Rows :----------")
print(df.head())

print("\n--------- : Last Two Rows : -----------")
print(df.tail(2))

print("\n-------- : DataFrame Info :---------")
df.info()

print("\n-------- : DataFrme Describtion : ---------")
print(df.describe())

# Info Provide total info about the dataframe :for example: info about its datatypes its size , memory usage , indexes info and how manydata are in column

# Description provide statistical info like count , mean , standard diviation , quantile , percentile , min and max