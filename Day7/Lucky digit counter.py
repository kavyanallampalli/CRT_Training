'''Lucky Digit Counter
Problem statement:
Given a number N,count how many times the digits 3 and 7
appear in it
Input Format:
A single integer N
Output Format:
Count of digits 3 and 7
Constraints:
1<=N<=10^12
Sample Input:
370731
Sample Output:
4'''




#Sum of count of 3 and 7 by user entered values
n=int(input())
n=list(str(n))
x=n.count('3')
y=n.count('7')
print(x+y)

#second method
n=input().strip()
print(sum(1 for d in n if d in ['3','7']))