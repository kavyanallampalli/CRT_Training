num=int(input("enter the integer:"))
res="four digit number" if((num>=1000 and num<=9999) or (num<=-1000 and num>=-9999)) else "non four digit number"
print(res)   
