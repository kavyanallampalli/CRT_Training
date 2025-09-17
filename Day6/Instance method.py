class Student:
    def __init__(self):
        print()
        print("Student Object is Created.....!")
        print()
    #mutator or setter methods
    def set_name(self,name):
        self.name=name
    def set_age(self,age):
        self.age=age
    def set_branch(self,branch):
        self.branch=branch
    #accessor or getter methods
    def get_name(self):
        print(f"Student Name is :{self.name}")
    def get_age(self):
        print(f"Student Age is :{self.age}")
    def get_branch(self):
        print(f"Student Branch is :{self.branch}")
S1=Student()
S1.set_name("Scott")
S1.set_age(21)
S1.set_branch("EEE")
S1.get_name()
S1.get_age()