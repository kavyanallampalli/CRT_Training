'''write a python program to read two integer values as input from 
the user and swap the values of the two integers
2.using the third variable'''




a=int(input("Enter the value of first integer : "))
b=int(input("Enter the value of second integer : "))
print(f"a={a}")
print(f"b={b}")
#Second Logic
temp=a
a=b
b=temp
print("After Swapping : ")
print(f"a={a}")
print(f"b={b}")