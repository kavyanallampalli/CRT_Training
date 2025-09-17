'''Count Vowels
Problem statement:
Count the number of vowels(a,e,i,o,u) in a given string
Input format:
A string S
Output Format:
Number of vowels
Sample Input:
codevita
Sample output:
4'''


#first method
string=input()
vowel=0
for ch in string:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowel+=1
print(vowel)


#second method
string=input().lower()
vowels="aeiou"
count=sum(1 for ch in string if ch.isalpha() and ch  in vowels)
print(count)
        