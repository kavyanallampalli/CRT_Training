'''write a python program to read three integer values as
input in same line and print the summation of integers'''


num=list(map(int,input("Enter the numbers :").split()))
print(num)
print(sum(num))