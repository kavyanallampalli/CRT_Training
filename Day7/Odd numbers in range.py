'''Odd Numbers in Range
Problem statement:
Print all odd numbers between L and R(inclusive)
Input format:
Two integers L and R
Output format:
Odd numbers separated by space
Sample Input:
3 10
Sample output:
3 5 7 9'''




n=int(input())
num=[]
for i in range(3,n+1):
    if i%2!=0:
        num.append(i)
print(num)