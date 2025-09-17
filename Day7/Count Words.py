'''Count Words
Problem Statement:
Count the number of words in a sentence
Input Format:
A sentence string
Output Format:
Word count
Sample input:
hello codevita world
Sample output:
3'''


Str=list(input().split())
words=0
for ch in Str:
    if ch.isalpha():
        words+=1
print(words)
    