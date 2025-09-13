'''write a python program to read the size of list
as input from the user and read the list element as
alphabetic characters and print the user entered
list and the sorted version of the user entered 
list.'''


size=int(input("Enter the size of the list :"))
chars=[]
for i in range(size):
    val=input("Enter the character at index {i}:")
    chars.append(val)
print("User Entered List :",chars)
sorted_list=sorted(chars)
print("Sorted List:",sorted_list)