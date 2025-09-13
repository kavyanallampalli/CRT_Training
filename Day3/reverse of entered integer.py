'''write a python program to read an integer value
as input from user and print reverse of it'''


n=int(input('Enter the value of n :'))
rem,rev=0,0
print(f"User entered number is {n}")
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(f"Reversed Number is {rev}")