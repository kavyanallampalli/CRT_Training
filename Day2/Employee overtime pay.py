'''Employee Overtime Pay
An employee works a standard 8 hours per day.
->If the employee works more than 8 hours,they get
100 per extra hour.
->If not,display "No overtime pay"
write a program that takes the number of hours
worked and prints the overtime pay if applicable.'''



hour=int(input("enter the hours"))
if hour>8:
    print(" 100 per extra hour")
else:
    print(" no overtime")
