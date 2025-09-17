'''Student Grades Analyzer 
Problem Statement:
A student’s grades in 3 subjects are given as a tuple. You need to:
1. Calculate the average marks.
2. Check if the student passed or failed.
Passing Rule:
• Average ≥ 40 and
• No subject has marks < 35
Input Format:
• 3 integers separated by space.
Output Format:
• Line 1: Average (up to 2 decimal places)
• Line 2: "Passed" or "Failed"
Constraints:
• 0 ≤ marks ≤ 100
Sample Test Cases:
Input 1:
45 50 30
Output 1:
41.67
Failed
Input 2:
60 70 50
Output 2:
60.0
Passed
Input 3:
35 35 35
Output 3:
35.0
Failed'''



marks=tuple(map(int,input("Enter 3 Subjects marks:").split()))
avg=sum(marks)/3
res=list(map(lambda i:i>=35,marks))
res="Failed" if( False in res) else "Passed"
print(f"Average :{avg}")
print(res)