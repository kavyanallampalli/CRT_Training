'''write a python program to print the even numbers from 
1 to n where n is the users input.'''



n=int(input('enter the integer value'))
print(f"Even Numbers from 1 to {n}")
for i in range(2,n+1,2):
    print(i)                                  
