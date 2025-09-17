'''Sum of unique elements
Problem statement:
Given a list of integers, find the sum of elements that appear only once
Input format:
First line:integer N
Second line:N space-separated integers
Output format:
Sum of unique elements
Constraints:
1<=N<=100
Sample input:
1 2 2 3 4 4
Sample output:
4'''


n=list(map(int,input().split()))
unique=sum(i for i in n if n.count(i)==1 )
print(unique)