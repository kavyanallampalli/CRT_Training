'''write a python program to print the natural 
numbers from n to 1 where n is the users input.'''



n=int(input('enter the integer value'))
print(f'Natural numbers from 1 to {n}')
for i in range(n,0,-1):
    print(i)                                
