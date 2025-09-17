'''Sales Data Analysis (Lists & 
Loops)
Problem Statement:
A shop records daily sales for a week in a list. You need to:
1. Find the maximum sales in a single day.
2. Find the total sales of the week.
Input Format:
• A single line of 7 integers (sales values).
Output Format:
• Line 1: Maximum sales
• Line 2: Total sales
Constraints:
• 1 ≤ sales ≤ 100000
Sample Test Cases:
Input 1:
200 450 300 500 700 150 400
Output 1:
700
2700
Input 2:
1000 2000 1500 800 1200 500 700
Output 2:
2000
7700'''



sales=list(map(int,input("Enter the sales for a week :").split()))
print(max(sales))
print(sum(sales))