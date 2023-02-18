n = int(input("Please Enter Length of Array : "))

list =[]
for i in range(n):
    element = float(input(f"Please Enter {i+1} th Element of Array : "))
    list.append(element)

print("Your Array is : ",list)
count = 0
for i in range(n):
    if list[i]==list[n-i-1]:
        count += 1

if count == n:
    print("Your Array is Regular")
else:
    print("Your Array is NOT Regular")