'''Sum of squares of digits
Problem statement:
Find the sum of squares of digits of a number N
Input format:
A single integer N
Output format:
Sum of squares of digits
Sample Input:
123
Sample Output:
14'''


num=list(map(int,input("Enter the numbers:").split()))
res=[i*i for i in num]
print(sum(res))