'''create a person class and declare the states as name,age,
gender,contact number,nationality,aadharnumber'''




class Person:
    def __init__(self,Name,Age,Gender,ContactNum,Nationality,AadharNum):
        self.Name=Name
        self.Age=Age
        self.Gender=Gender
        self.ContactNum=ContactNum
        self.Nationality=Nationality
        self.AadharNum=AadharNum
    def display(self):
        print(f"Person Name is : {self.Name}")
        print(f"Person Age is : {self.Age}")
        print(f"Gender is : {self.Gender}")
        print(f"ContactNum is : {self.ContactNum}")
        print(f"Nationality is : {self.Nationality}")
        print(f"Person AadharNum is : {self.AadharNum}")
E1=Person("Chinna",20,"Male",9876507234,"Indian",325089765437)
E1.display()
        
        