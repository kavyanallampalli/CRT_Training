'''write a python program to print the sum of 
natural numbers from 1 to n'''


n=int(input('Enter the value of n:'))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(f"Summation is{sum}")    
