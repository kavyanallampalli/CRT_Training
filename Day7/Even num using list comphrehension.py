'''write a python program to print the list of even numbers
from 1 to n using list comprehension'''



n=int(input("enter the value"))
num=[]
for i in range(1,n+1):
    if i%2==0:
        num.append(i)
print(num)
