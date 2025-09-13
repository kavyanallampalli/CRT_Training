'''write a python program to print the multiplication
table of n using functions.'''


def table(n):
    print(f"Multiplication table of {n} \n")
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
    print()
table(4)
table(5)
table(3)

    