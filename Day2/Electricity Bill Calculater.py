'''Electricity Bill Calculator
Electricity unit charges are:
-> First 100 units==>5 per unit
-> Next 100 units==>7 per unit
-> Above 200 units==>10 per unit
Write a program that takes units consumed as input
and prints the total bill.'''


units=int(input('enter the units :'))
if units<=100:
    bill=units*5
elif units<=200:
    bill=units*7
else:
    bill=units*10
print(f"total bill={bill}")              
