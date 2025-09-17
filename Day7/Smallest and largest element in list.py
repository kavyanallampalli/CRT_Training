'''Smallest and Largest Element in List
Problem statement:
Given N numbers, print the smallest and largest element
Input format:
First line:Integer N
Second line:list of N integers
Output format:
Two integers:smallest and largest element
Sample input:
12 5 8 20 7
Sample output:
5 20'''



num=list(map(int,input().split()))
print(max(num))
print(min(num))