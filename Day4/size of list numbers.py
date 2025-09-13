'''write a python program to read the size of list
as input from the user and read the list element
as input from the user and print the user entered
list.'''


size=int(input("Enter the size of the list:"))
Num=[]
for i in range(size):
    val=int(input("Enter the element at {i} index :"))
    Num.append(val)
print("User Entered List :")
print(Num)