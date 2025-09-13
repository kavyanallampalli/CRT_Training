'''write a python program to print the multiplication
table of n.'''


n=int(input('enter the value of n:'))
print(f"Multiplication Table of {n}")
for i in range(1,11):
   print(f"{n} x {i} = {n*i}")                                           
