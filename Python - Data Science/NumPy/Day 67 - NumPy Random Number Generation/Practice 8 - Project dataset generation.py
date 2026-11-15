import numpy as np
np.random.seed(42)
study_hours = np.random.uniform(1,10,size=10)
attendance = np.random.randint(50,100,size=10)
marks = np.random.randint(0,101,size=10)

dataset=np.column_stack(
    (study_hours ,
     attendance,
     marks
     )
)
average=np.mean(dataset[:,2])
print("--------------: Student Info :------------")
print(dataset)
print(dataset.shape)
print("Average Marks of Students :",average)
print("Student Info Who Scored 50 or greater :\n",dataset[dataset[:,2] >= 50])


