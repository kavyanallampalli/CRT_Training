'''write a python program to print the count 
of digits present in the user entered number.'''



n=int(input('Enter the value of n:'))
digit_count=0
while(n!=0):
    n=n//10
    digit_count+=1
print(f"Digit count is{digit_count}")    