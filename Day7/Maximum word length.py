'''Maximum Word Length
Problem Statement:
Find the length of the longest word in a sentence
Input Format:
A sentence string
Output Format:
Length of the longest word
Constraints:
Sentence length<=200
Sample Input:
codevita makes programming fun
Sample Output:
11'''


Str=list(input().split())
print(Str)
print(len(max(Str,key=len)))
