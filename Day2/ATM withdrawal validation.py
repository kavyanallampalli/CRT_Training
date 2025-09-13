'''ATM withdrawal validation
You are designing an ATM system. A customer enters 
the amount to withdraw.
->The withdrawal must be less than or equal to the
account balance(5000).
->The amount must be multiplies of 100.
->If the both conditions are satisfied,allow 
withdrawal.
->Otherwise, display an appropriate error message
(e.g:-"Insufficient balance" or "Amount should be
multiple of 100")'''



amt=int(input("enter the amount "))
acc_balance=5000
if(amt<=acc_balance and amt%100==0):
    print("allow withdraw")
else:
  print("insufficient balance")   
