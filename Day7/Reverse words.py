'''Reverse Words
Problem statement:
Given a sentence, print its words in reverse order without
reversing the characters inside words
Input Format:
A single sentence string
Output Format:
Words in reverse order
Sample input:
welcome to codevita
Sample Output:
codevita to welcome'''



s=input().split()
print(" ".join(list(map(lambda i:s[-i-1],range(len(s))))))
