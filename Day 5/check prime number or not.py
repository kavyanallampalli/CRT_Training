'''write a python program to check whether the user entered integer
is a prime number or not'''



num=int(input("Enter the integer value:"))
factor=0
for i in range(1,num+1):
    if(num%i==0):
        factor+=1
res="Prime Number" if(factor==2) else "Not a prime number"
print(res)