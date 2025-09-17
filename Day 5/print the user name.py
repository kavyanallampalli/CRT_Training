'''write a python program to read the name of the user and print the 
length of the name and check if it is more than 5 characters''' 



name=input("Enter your name :")
print("Length of name :",len(name))
res="More than 5 characters" if(len(name)>5) else "Not more than 5 characters"
print(res)