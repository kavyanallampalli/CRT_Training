'''Train Ticket Concession
Indian Railways provide fare concessions:
->Children below 5 years==>Free
->5-12 years==>Half Ticket
->13-59==>Full Ticket
->60+ years==>30% Senior Citizen Discount
write a program to decide the fare type based on age.'''



age=int(input("enter the age :"))
if age<=5:
    print("Free")
elif age>=5 and age<=12:
    print("Half Ticket")
elif age>=13 and age<=59:
    print("Full Ticket")
else:
   print("30% Senior Citizen Discount")
