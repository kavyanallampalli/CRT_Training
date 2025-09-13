'''write a python program to find the factorial of 
n'''


n=int(input('Enter the value of n: '))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f"Factorial of {fact}")    