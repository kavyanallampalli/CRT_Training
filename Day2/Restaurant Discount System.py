'''Restaurant Discount System
A restaurant gives discounts based on the total bill:
->If bill>1000==>10% discount
->If bill>500==>5% discount
->If bill<=500==>No discount
write a program that calculates and displays the 
final amount after discount.'''



bill=int(input("enter the total bill"))
if bill>1000:
    discount=bill*0.10
elif bill>500:
    discount=bill*0.5
else:
    discount=0
final_amount =bill-discount
print(f"Original bill: {bill}")
print(f"discount : {discount}")
print(f"Final amount to pay : {final_amount}")          
