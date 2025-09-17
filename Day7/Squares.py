'''write a python program to read a list of elements as input
from the user and print the square values of list elements
without loops
sample test case:
enter the numbers:[2,4,6,7,8,10]
squared list:[4,16,36,49,64,100]'''



#first method
num=list(map(int,input("Enter the elements :").split()))
print(num)
square=lambda :[val*val for val in num]
print(square())



#second method
num=list(map(int,input("Enter the elements :").split()))
square=list(map(lambda i:i*i,num))
print(square)


#third method
size=int(input("Enter the size of list:"))
List=[]
New=[]
for i in range(size):
    val=int(input("Enter the value:"))
    List.append(val)
print(List)
for i in List:
    i=i*i
    New.append(i)
print(New)