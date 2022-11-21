x=int(input("Enter A Integer Number : "))
y=int(input("Enter An Other Integer Number : "))

if x > y:
    greater = x
else:
    greater = y

while(True):
    if ((greater % x == 0) and (greater % y == 0)):
        lcm = greater
        break
    greater += 1



print(f"The Least Common Multiple of {x} and {y} is {lcm}")