'''write a python program to read an integer value as input from the 
user and check whether it is a prime palindrome or not'''



num=int(input("Enter the integer value"))
factor=0
pn=num
rev,rem=0,0
while(pn!=0):
    rem=pn%10
    rev=rev*10+rem
    pn=pn//10
if(num==rev):
    for i  in range(1,num+1):
        if(num!=0):
            factor+=1
res="Prime Palindrome" if(factor==2 and num==rev) else "Not a Prime Palindrome"
print(res)