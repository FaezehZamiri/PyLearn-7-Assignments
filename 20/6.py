import random

boys = ["mohammad", "sobhan", "abdollah", "kiya", "mahdi", "sajjad", "homan", "arman"]
girls = ["mahtab", "hane", "harir", "fateme", "kiana", "faezeh", "minoo", "mina", "soghra"]

result=[]
while 0 < len(boys):
    boy = random.choice(boys)
    girl = random.choice(girls)
    result.append((boy,girl))
    boys.remove(boy)
    girls.remove(girl)


print(result)