'''Even Odd Rearrangement
Problem statement:
Rearrange integers so that even numbers come first, then odd
numbers. Order must be preserved in both groups
Input Format:
First line:integer N
Second line:N space-separated integers
Output Format:
Rearranged list
Constraints:
1<=N<=100
Sample Input:
3 2 4 7 10 5
Sample Output:
2 4 10 3 7 5'''



nums=list(map(int,input().split()))
res=[x for x in nums if x%2==0]+[x for x in nums if x%2!=0]
print(res)