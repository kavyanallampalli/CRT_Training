'''GCD of Two Numbers
Problem statement:
Find the greatest common divisor(GCD) of two given numbers
Input format:
Two integers A and B
Output format:
GCD of A and B
Sample input:
12 18
Sample output
6'''


import math
a,b=list(map(int,input().split()))
print(math.gcd(a,b))