'''Fitness BMI Checker
You are building a fitness app that checks BMI category:
->BMI<18.5==>Underweight
->18.5<=BMI<25==>Normal weight
->25<=BMI<30==>Overweight
->BMI>=30==>Obese
Write a program that asks BMI as input and displays
the category.'''



BMI=int(input("enter the weight :"))
if BMI<18.5:
    print("Underweight")
elif BMI>=18.5 and BMI<25:
    print("Normal weight")
elif BMI>=25 and BMI<30:
    print("Overweight")
else:
    print("Obese")                                               
