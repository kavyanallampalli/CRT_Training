'''write a python program to print the multipplication 
tables from 1 to n where as n is an integer input from the user.'''



n=int(input('enter the value of n:'))
for i in range(1,11):
    for j in range(1,n+1):
        print(f"{j} x {i}= {j*i}", end="\t")
    print()                                                
