class Student:
    def __init__(self,name,age,branch):
        self.StdName=name
        self.Age=age
        self.Branch=branch
    def display(self):
        print(f"Student Name is :{self.StdName}")
        print(f"Student Age is : {self.Age}")
        print(f"Student Branch is : {self.Branch}")
S1=Student('Scott',20,'CSE')
S1.display()
S2=Student('Adams',21,'ECE')
S2.display()
        