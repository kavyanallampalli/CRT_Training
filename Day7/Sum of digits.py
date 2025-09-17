'''Sum of Digits
Problem statement:
Given an integer N,find the sum of its digits
Input format:
A single integer N
Output format:
Sum of digits
Sample input:
12345
Sample output:
15'''



num=list(map(int,input("Enter the numbers :").split()))
print(sum(num))