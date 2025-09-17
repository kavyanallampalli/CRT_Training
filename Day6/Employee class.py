'''write a python program to check an employee class and declare
the states as employee name,employee number,designation,salary,
dept num create 5 objects and access the details of 5 objects
of employee using functions'''



class Employee:
    def __init__(self,EmpName,EmpNum,Designation,Salary,Deptnum):
        self.EmpName=EmpName
        self.EmpNum=EmpNum
        self.Designation=Designation
        self.Salary=Salary
        self.Deptnum=Deptnum
    def display(self):
        print(f"Employee Name is : {self.EmpName}")
        print(f"Employee Number is : {self.EmpNum}")
        print(f"Employee Designation is : {self.Designation}")
        print(f"Employee Salary is : {self.Salary}")
        print(f"Employee Deptnum is : {self.Deptnum}")
E1=Employee("Chinna",123,"Developer",50000,765)
E1.display()
        
        