class Person:
    def __init__(self,Name,Age,Gender):
        print("Person Class Object is Created")
        self.Name=Name
        self.Age=Age
        self.Gender=Gender
class Student(Person):
    def __init__(self,Name,Age,Gender,Id,Branch):
        super().__init__(Name, Age, Gender)
        self.Id=Id
        self.Branch=Branch
        print("Student class object is created")
s1=Student(1,2,3,4,5)