n = int(input("Enter number of elements : "))
lst = []
print("Now enter elements one by one :")
for i in range(n):
    ele = int(input())
    lst.append(ele) 
     
print(lst)
for i in range (n):
    if lst[i-1] <= lst[i]:
        c=1
    else:
        c=0
if c==1:
    print("list is sorted")  
else:
    print("list is not sorted")  
