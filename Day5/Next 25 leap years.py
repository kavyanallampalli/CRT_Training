'''write a python program to print the next 25 leap years
from the user entered year'''

year=int(input("Enter a starting year :"))
count=0
print("Next 25 leap years are:")
while count<25:
    if(year%4==0 and year%100!=0) or (year%400==0):
        print(year)
        count+=1
    year+=1
    