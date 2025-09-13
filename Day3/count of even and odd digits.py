'''write a python program to print the count of 
even digits and odd digits present in the user
given number.'''



n=int(input('Enter the value of n:'))
even,odd,rem=0,0,0
while(n!=0):
    rem=n%10
    if rem%2==0:
        even+=1
    else:
        odd+=1
    n=n//10
print(f"Even Digit Count is {even}")
print(f"Odd Digit Count is {odd}")