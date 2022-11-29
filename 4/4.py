n =int(input("Please Enter the Length of List :"))
  
myList = []
for i in range(n):
    member = float(input(f"Enter {i+1}th Number : "))
    myList.append(member)

print(myList) 

newList = []
for j in range(1,len(myList)+1):
    newList.append(myList[-j])

print(newList) 

