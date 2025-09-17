'''LCM of Two Numbers
Problem statement:
Find the least common multiple(LCM) of two given numbers
Input format:
Two integers A and B
Output format:
LCM of A and B
Sample input:
12 18
Sample output
36'''



import math
a,b=list(map(int,input().split()))
print(math.lcm(a,b))