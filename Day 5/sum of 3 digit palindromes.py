'''write a python program to print all three digit palindrome numbers'''


total=0
for i in range(100,1000):
    if str(i)==str(i)[::-1]:
        total+=i
print(total)


for i in range(1,10):
    for j in range(0,10):
        print(f"{i}{j}{i}",end=",")