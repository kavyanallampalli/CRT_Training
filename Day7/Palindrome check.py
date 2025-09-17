'''Palindrome check
Problem statement:
check whether a given string is a palindrome or not.Ignore 
case sensitivity
Input Format:
A string S
Output Format:
YES if palindrome,else NO
Sample input:
Level
Sample Output:
YES'''



s=input().lower()
res="Yes" if s==s[::-1] else "No"
print(res)
