'''write a python program to read two integer values as input from 
the user and swap the values of the two integers
1.Arithmetic operations'''



a=int(input("Enter the value of first integer : "))
b=int(input("Enter the value of second integer : "))
print(f"a={a}")
print(f"b={b}")
#First Logic
a=a+b
b=a-b
a=a-b
print("After Swapping :")
print(f"a={a}")
print(f"b={b}")