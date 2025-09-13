'''Water Remainder App
You are building a water remainder.Input is the 
number of hours since the user last drank water.
->  >=4 hours==>"You are dehydrated! Drink water now!"
->  Between 2-3 hours==>"Drink  a glass of water"
->  Lessthan 2 hours==>"You are fine"'''


hour=int(input("enter the hours"))
if hour>=4:
    print("you are dehydrated! drink water now")
elif hour>=2 and hour<=3:
    print("drink a glass of water")
else:
    print("you are fine") 
