name=input("What is your name? ")
family=input("What is your family name? ")
point1=float(input("Enter your 1st Point: "))
point2=float(input("Enter your 2ed Point: "))
point3=float(input("Enter your 3th Point: "))

ave=(point1+point2+point3)/3

if ave<12:
    print(f"{name} {family},your average is {ave} and you are fail")
elif ave>=12 and ave<17:
    print(f"{name} {family},your average is {ave} and you are normal")
elif ave>=17:
    print(f"{name} {family},your average is {ave} and you are great")
