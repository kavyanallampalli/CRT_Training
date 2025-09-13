'''write a python program to print the second maximum
number present in the list of numbers.'''



num=[55,92,75,10,47]
unique_numbers=list(set(num))
unique_numbers.sort()
print("Second Maximum Number:",unique_numbers[-2])
