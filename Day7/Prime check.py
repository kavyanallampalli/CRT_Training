'''Prime check
Problem statement:
Check if a given number N is a prime number:
Input format:
A single integer N
Output Format:
YES if prime, else NO
Sample input:
7
Sample Output:
YES'''


prime = lambda n:n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))
n=int(input())
print(prime(n))