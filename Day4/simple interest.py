'''write a python program to calculate the simple
interest by using a parameterized function.'''


def cal_interest(amount,rateofinterest,time):
    interest=(amount*rateofinterest*time)/100
    print(f"Simple Interest : {interest}")
cal_interest(10000,2,2)