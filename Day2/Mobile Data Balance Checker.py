'''Mobile Data Balance Checker
A telecom operator shows messages based on data
balance:
->If balance=0MB==>"Recharge required"
->If balance<=100MB==>"Low data warning"
->Otherwise==>"Sufficient data available"
write a program to check users data balance.'''


data=int(input('enter the data balance :'))
if data==0:
    print("Recharge Required")
elif data<=100:
    print("Low data Warning")
else:
    print("Sufficient data available")   
