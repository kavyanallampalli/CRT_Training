'''Count Digits and Alphabets
Problem statement:
Given a string,count the number of digits and alphabets separately.
Ignore other characters
Input format:
A string S
Output format:
Two integers:count of alphabets and count of digits
Sample input:
codevita2025
Sample output:
8 4'''



string=input()
digit,alphabet=0,0
for ch in string:
    if ch.isdigit():
        digit+=1
    elif ch.isalpha():
        alphabet+=1
print(digit)
print(alphabet)
