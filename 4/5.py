n =int(input("Please Enter the Length of List :"))
  
myList = []
for i in range(n):
    member = float(input(f"Enter {i+1}th Number : "))
    if member not in myList:
        myList.append(member)

print(myList) 

