from math import factorial as fact 
n=int(input('Enter an intiger Number : '))
a=[]
for i in range(n):
    for j in range(i+1):
        number = fact(i) / (fact(j) * fact(i-j))
        a.append(number)
    print(a)
    a.clear()