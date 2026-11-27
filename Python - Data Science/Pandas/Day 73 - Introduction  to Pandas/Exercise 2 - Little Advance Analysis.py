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
print("------: Name Column :------")
print(df.Name)

print("\n-------: Name and Marks :----------")
print(df[['Name','Marks']])

print("\n-----------: Student WIth Highest Marks :-------------")
index = df.Marks.idxmax()
print(df['Name'][index])

print("\n--------: Student With Lowest Marks :-------- ")
index = df.Marks.idxmin()
print(df['Name'][index])

print("\n---------: Students Marks greater then 80 :------------")
print(df[df['Marks'] > 80])

print("-------: Average Age :--------")
print(df.Age.mean())