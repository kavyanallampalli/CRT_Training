'''write a python program to print the odd
numbers from n to 1.'''



n=int(input('enter the integer value'))
print(f"Odd numbers from 1 to {n}")
for i in range(n,0,-1):
    if(i%2==0):
        print(i)                                         
