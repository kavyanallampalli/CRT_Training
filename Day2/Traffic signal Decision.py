'''Traffic signal decision
create a program that takes the current traffic light
color(Red,Yellow and Green) as input
->If the light is Red=>Display"Stop immediately"
->If the light is Yellow=>Display"Get Ready to Move"
->If the light is Green=>Display"You can go"'''



n=input("enter the signal colour").lower()
if n=="red":
    print("stop immediately")
elif n=="yellow":
    print("get ready to move")
elif n=="green":
    print("you can go")     