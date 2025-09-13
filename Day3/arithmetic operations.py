'''write a python program to read two integer values
 as input from the user and perform the arthimetic
 operations based on following conditions.
1.Addition
2.Substraction
3.Multiplication
4.Division
5.Exit
Iterate the loop until the user chooses 
the file to exit.'''


a=int(input('enter the first value :'))
b=int(input('enter the second value :'))
while(True):
    print("_______Operations Menu_______")
    print("Addition")
    print("Substraction")
    print("Multiplication")
    print("Division")
    print("Exit")
    choice=int(input('Enter your choice :'))
    if(choice==1):
        print(f"Summation of {a},{b} is {a+b}")
        print()
    elif(choice==2):
        print(f"Difference of{a},{b} is {a-b}")
        print()
    elif(choice==3):
        print(f"Product of {a},{b} is{a*b}")
        print()
    elif(choice==4):
        print(f"Quotient of {a},{b} is{a/b}")
        print()
    elif(choice==5):
        print(f"Thanks for using the Operations Menu")
        break
        
