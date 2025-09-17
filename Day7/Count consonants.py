'''Count Consonants
Problem statement:
Count the number of consonants in a given string
Input format:
A string S
Output Format:
Number of vowels
Sample Input:
codevita
Sample output:
4'''




string=input().lower()
vowels="aeiou"
count=sum(1 for ch in string if ch.isalpha() and ch not in vowels)
print(count)
        