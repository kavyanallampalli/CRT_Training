'''write a python program to read a list of numbers and print
the list of even numbers and odd numbers without using
loops and conditional statements'''



num=list(map(int,input("Enter the numbers:").split()))
even=list(filter(lambda i:i%2==0,num))
odd=list(filter(lambda i:i%2!=0,num))
print(f"User Entered List :{num}")
print(f"Even List :{even}")
print(f"Odd List :{odd}")
