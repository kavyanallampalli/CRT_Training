'''write a python program to print the even numbers 
from n to 1.'''



n=int(input('Enter the integer value' ))
print(f"Even numbers from 1 to {n}")
for i in range(n,0,-1):
    if(i%2==0):
       print(i)                                    
