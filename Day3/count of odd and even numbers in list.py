'''write a python program to print the count of even
numbers and odd numbers present in the list.'''



num=[10,15,20,25,30,35,40]
even_count=sum(1 for n in num if n%2==0)
odd_count=sum(1 for n in num if n%2!=0)
print(f"Even Numbers count : {even_count}")
print(f"Odd Numbers count : {odd_count}")
