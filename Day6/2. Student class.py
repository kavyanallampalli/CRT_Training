''''''




#variable
class Student:
    def __init__(self,name,age,branch):
        self.StdName=name
        self.Age=age
        self.Branch=branch
S1=Student("Scott",20,"CSE")
S2=Student("Kavya",21,"CSD")
print(f"Student Name is: {S1.StdName,S2.StdName}")
print(f"Student Age is: {S1.Age,S2.Age}")
print(f"Student Branch is: {S1.Branch,S2.Branch}")

#create 3 more objects
