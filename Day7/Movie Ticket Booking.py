'''Movie Ticket Booking 
Problem Statement:
A cinema hall charges tickets based on age:
• Age ≤ 12 → ₹150
• 13 ≤ Age ≤ 59 → ₹250
• Age ≥ 60 → ₹200
Given a list of ages, calculate the total ticket cost.
Input Format:
• A single line of integers (ages of people).
Output Format:
• Total ticket cost.
Constraints:
• 1 ≤ number of people ≤ 20
• 1 ≤ age ≤ 100
Sample Test Cases:
Input 1:
10 14 25 65
Output 1:
850
Input 2:
5 35 70 12 60
Output 2:
950
Input 3:
15 40 8
Output 3:
650'''



ages=list(map(int,input("Enter the Ages :").split()))
total_cost=0
for age in ages:
    if age<=12:
        total_cost+=150
    elif age>=60:
        total_cost+=200
    else:
        total_cost+=250
print(total_cost)