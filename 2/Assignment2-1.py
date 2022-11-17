import random

PCNumber = random.randint(10,40)
n=1
while True:
    YourNumber=int(input("Please Enter a Integer Number: "))
    if YourNumber == PCNumber:
        print('You Win!')
        break
    elif YourNumber >= PCNumber:
        print('Go Down!')
        n=n+1
        continue
    else:
        print('Go Up!')
        n=n+1
        continue
    
print(f"You Guess {n} Time!")


