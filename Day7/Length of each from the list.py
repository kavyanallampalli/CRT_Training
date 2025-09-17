'''write a python program to read the list of words as input
from the user and return the length of each word for the list'''



size=int(input("Enter the size of list:"))
WordList=[]
for i in range(size):
    val=input("Enter the word:")
    WordList.append(val)
print("User Entered List is :",WordList)
Len=list(map(lambda w:len(w),WordList))
print("Length of the Words in the List :",Len)