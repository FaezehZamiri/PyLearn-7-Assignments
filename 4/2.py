n = int(input('Please Enter an Positive Integer Number : '))

i=1
j=1
while j<n:
    i=i+1
    j=j*i
if j == n:
    print(f"{n} is a Factorial of {i}")
else:
    print(f"{n} is Not Factorial")