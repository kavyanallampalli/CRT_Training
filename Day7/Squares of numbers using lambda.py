'''write a python program to square the numbers in the
list using lambda functions'''


num=[1,2,3,4,5,6,7,8,9,10]
square=lambda :[val*val for val in num]
print(square())