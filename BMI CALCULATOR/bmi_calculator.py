import sys
import time

print("Hello there!","Do you want to calculate your BMI?")
time.sleep(3)
print("Yes")
time.sleep(1)
print("No")
time.sleep(2)
choice=input("Your Choice: ")
if choice=="Yes" :
    print("Ok then, help us by providing some information")
    height=float(input("Enter your Height in Meter: "))
    weight=float(input("Enter your Weight in KG: "))
    bmi=weight/(height*height)
    if bmi<18.5 :
        print("Your BMI is:",bmi)
        print("And your condition is Underweight")
    elif 18.5<= bmi <25 :
        print("Your BMI is:",bmi)
        print("And your condition is Normal")
    elif 25<= bmi <30 :
        print("Your BMI is:",bmi)
        print("And your condition is Overweight")
    else:
        print("Your BMI is:",bmi)
        print("And your condition is Obesity")
else:
    sys.exit()
        
