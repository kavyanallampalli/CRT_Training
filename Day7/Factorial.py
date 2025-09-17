'''Factorial
Problem statement:
Find the factorial of a given number N
Input format:
A single integer N
Output format:
Factorial of N
Sample input:
5
Sample output:
120'''


#first method
n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)


#second method
import math
n=int(input())
print(math.factorial(n))