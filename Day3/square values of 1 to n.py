'''write a python program to print the square values
of 1 to n using for loop and while loop'''


n=int(input('Enter the value :'))
for i in range(1,n+1):
    print(i*i)
#using while
i=1
while(i<=n):
    print(i*i)
    i+=1
    