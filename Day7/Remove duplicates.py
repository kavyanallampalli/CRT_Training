'''Remove Duplicates
Problem statement:
Given a list of integers, remove all duplicates while 
preserving the order of first occurance
Input format:
First line:integer N
Second line:N space-separated integers
Output format:
List without duplicates
Sample input:
1 2 2 3 4 3
Sample output:
1 2 3 4'''


n=list(map(int,input().split()))
unique=list(set(n))
s=' '.join(map(str,unique))
print(s)