'''write a python program to print the reversed 
multiplication table of n.'''


n=int(input('enter the value of n:'))
print(f"Multiplication Table of {n}")
for i in range(10,0,-1):
   print(f"{n} x {i} = {n*i}")                                               
