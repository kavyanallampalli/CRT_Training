'''write a python program to print the odd numbers 
from 1 to n. '''



n=int(input("enter the integer value"))
print(f"Odd numbers from 1 to {n}")
for i in range(1,n+1,2):
    print(i)                                      
