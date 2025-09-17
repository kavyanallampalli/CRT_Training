'''write a python program to square the numbers in the 
list using lambda functions'''




num=[1,2,3,4,5,6,7,8,9,10]
def double(n):
    return n*n
res=list(map(double,num))
print(res)