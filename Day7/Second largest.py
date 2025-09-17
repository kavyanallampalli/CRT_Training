'''Second Largest
Problem statement:
Given N numbers,find the second largest unique number
Input format:
First line:N space-separated integers
Output format:
The second largest number
Sample input:
10 30 20 50 40
Sample output:
40'''



num=list(map(int,input().split()))
unique_number=list(set(num))
unique_number.sort()
print(unique_number[-2])