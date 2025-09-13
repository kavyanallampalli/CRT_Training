'''Movie Ticket Pricing
In a theater, ticket prices vary depending an the
customers age:
->Children below 12 years==> 150
->Teenagers below 12 and 18 years==>200
->Adults above 18 years==>300
Write a program that asks the users age and prints 
the correct ticket price.'''



age=int(input("enter the age"))
if age<=12:
    print("150")
elif age>=12 and age<=18:
    print("200")
else:
   print("300")                                        
