'''Count Distinct Elements
Problem statement:
Count how many distinct elements are present in a list
Input format:
First line:integer N
Second line:list of N integers
Output format:
Number of distinct elements
Sample input:
1 2 2 3 4 4 5
Sample output:
5'''



n=list(map(int,input().split()))
count=len(set(n))
print(count)

