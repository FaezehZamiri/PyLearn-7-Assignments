import random
n=int(input("Enter A Integer Number: "))
numbers=[]
if n>0:
    a=random.randint(1,100)
    numbers.append(a)
    while len(numbers)<=n-1:
        c=random.randint(1,100)
        for i in range(len(numbers)):
            if c != numbers[i]:
                numbers.append(c)
                break

print(numbers)


