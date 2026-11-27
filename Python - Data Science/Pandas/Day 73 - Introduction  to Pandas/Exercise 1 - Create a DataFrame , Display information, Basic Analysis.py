import pandas as pd

students = {
    "Name" :["Farhan Ali" , "Asad Khan" , 
             "Ashraf Ali" , "Aziz Khan ",
               "Ihtisham Ahmed"],
    "Age"  :[21 , 20 , 22 , 23 , 19],
    "Marks":[89 , 90 , 87 ,50 ,58],
    "Semester":[5,5,5,5,5]
}
df =pd.DataFrame(students)

# Display Information
print("================ DISPLAY INFORMATION ==================")
print("------: Student DataFrame :-----\n",df)
print("-----: First Two Row :-----")
print(df[:2])
print("----: Last Two Rows :----")
print(df[3:])
print("Shape :",df.shape)

print("\n==================== Basic Analysis ====================")
print("Mean of Marks  :",df["Marks"].mean())
print("Maximum Marks  :",df["Marks"].max())
print("Minimum Marks  :",df["Marks"].min())
print("Total Students :",df.shape[0])

# Pandas is a Python Library that is used for data manipulation and analysis 
# Help in reading CSV data and excel files
# Handle missing values
# Calculate Statistic 
# Clean real world datasets

#Data frame is organize data that was easy to read and manipulate and porform other operation on it

# NumPy deal only with arrays to perform operation on array statistic and dataanlasis on the other hand pandas help to read csv and excel files and other files to perform operation on it
# Because we use a easy elise to access pandas

