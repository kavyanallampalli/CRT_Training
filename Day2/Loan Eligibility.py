'''Loan Eligibility 
A bank checks loan eligibility:
->Salary>=30000 and Credit Score>=700==>Eligible
->Otherwise==>Not Eligible
write a program that takes salary and credit score 
and decides eligibility.''' 



salary=int(input("enter the salary :"))
credit_score=int(input("enter the credit_score :"))
if salary>=30000 and credit_score>=700:
    print("Eligible")
else:
    print("Not Eligible")                                              
