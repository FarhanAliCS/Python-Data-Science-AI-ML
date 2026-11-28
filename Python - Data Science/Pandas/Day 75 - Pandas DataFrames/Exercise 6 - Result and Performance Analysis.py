import pandas as pd

students = {
    "Name": ["Ali", "Ahmed", "Sara", "Usman", "Ayesha", "Bilal"],
    "Age": [20, 21, 19, 22, 20, 23],
    "Marks": [85, 90, 95, 70, 88, 55],
    "Semester": [3, 4, 3, 5, 4, 6],
    "Department": [
        "CS", "SE", "CS", "IT", "CS", "SE"
    ],

}

#=================================================

#Create a DataFrame
df = pd.DataFrame(students)
print("=" * 50)
print("          Students DataFrame")
print("=" * 50)
print(df)


# Create a result column if marks >= 60 pass else Fail
df["Result"] = "Fail"
df.loc[df["Marks"] >= 60 , "Result"] = "Pass"

# Performace column

df["Performance"] = "Poor"
df.loc[df["Marks"] >= 90 , "Performance"] = "Excellent"
df.loc[(df["Marks"] >=80) & (df["Marks"] < 90) ,"Performance"] = "Good"
df.loc[(df["Marks"] >= 60) & (df["Marks"] < 80) , "Performance"] = "Average"

print("\n"+"="*65)
print("          Update DataFrame")
print("="*65)
print(df)


