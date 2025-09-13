'''write a python program to check the user entered
integer is a palindrome number or not'''


n=int(input("Enter the value of n :"))
temp=n
rev=0
print(f"Users given number is :{n}")
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(f"Reversed Number is {rev}")
if (temp==rev):
    print("Palindrome ")
else:
    print("Not a Palindrome")
