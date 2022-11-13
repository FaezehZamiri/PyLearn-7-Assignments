weight=float(input("PlS Enter Your Weight (in Kilogram): "))
height=float(input("PlS Enter Your Height (in Centimeter): "))

BMI=weight/(height/100)**2

if  BMI < 18.5:
    print(f"Your BMI is {BMI} and YOU are UnderWeight")
elif BMI >= 18.5 and BMI<25:
    print(f"Your BMI is {BMI} and YOU are Normal")
elif BMI >= 25 and BMI<30:
    print(f"Your BMI is {BMI} and YOU are OverWeight")
elif BMI >= 30 and BMI<35:
    print(f"Your BMI is {BMI} and YOU are Obese")
elif BMI >= 35:
    print(f"Your BMI is {BMI} and YOU are Extremely Obese")


