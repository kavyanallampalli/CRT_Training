'''Temperature Alert System
Based on the given temperature(in C)
->  <0==>"Freezing weather
->  0-20==>"Cold weather"
->  21-35==>"Normal weather"
->  35==>"Hot weather"
write a program that classifies temperature'''


temp=int(input("enter the temperature: "))
if temp<0:
    print("Freezing Weather")
elif temp>=0 and temp<=20:
    print("Cold Weather")
elif temp>=20 and temp<=35:
    print("Normal Weather")
else:
    print("Hot Weather")                                          
