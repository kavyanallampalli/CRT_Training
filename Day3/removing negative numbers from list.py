'''write a python program to remove the negative 
numbers the list of numbers.'''


num=list(map(int,input('Enter the numbers separated by space:').split()))
positive_numbers=[]
for i in num:
    if i>=0:
        positive_numbers.append(i)
print("List after removing negative numbers:",positive_numbers)

num=[10,-5,20,-15,30,-25,40]
print(num)
positive_numbers=[i for i in num if i>=0]
print("List after removing negatives:",positive_numbers)