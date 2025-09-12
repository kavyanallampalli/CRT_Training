num1=int(input("enter the first integer:"))
num2=int(input("enter the second integer:"))
num3=int(input("enter the third integer:"))
largest=num1 if(num1>num2 and num1>num3) else num2
res=num3 if(num3>num1 and num3>num2) else largest
print(f"{res} is the largest number")       
