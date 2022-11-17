import random
n=int(input('How many times do you want to roll the dice? '))

for i in range(n):
    d=random.randint(1,6)
    print(f"{i+1}th Chance is {d}")
    while d==6:
        d=random.randint(1,6)
        print(f"second Chance is {d} \U0001f600")
        i=i+1
        n=n+1



