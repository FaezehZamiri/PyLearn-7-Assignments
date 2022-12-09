from pyfiglet import Figlet
import qrcode

def show_menu():
    print("1-Add Product")
    print("2-Edit Product")
    print("3-Delete Product")
    print("4-Search")
    print("5-Show List")
    print("6-Buy")
    print("7-Make QRCode")
    print("8-Exit")
def show_list():
    print(f"The Products List Are : ")
    print('id'+'\t'+'Name'+'\t\t'+'Price'+'\t'+'Count')
    for i in range(len(Products)):
        print(str(Products[i]['id'])+'\t'+Products[i]['Name']+'\t\t'+str(Products[i]['Price'])+'\t'+str(Products[i]['Count']))
Products=[]
def load():
    data=open("database.txt",'r')
    data=data.read()
    productList=data.split("\n")
    for i in range(len(productList)):
        productInfo=productList[i].split(",")
        myDict={}
        myDict['id']=int(productInfo[0])
        myDict['Name']=productInfo[1]
        myDict['Price']=float(productInfo[2])
        myDict['Count']=int(productInfo[3])
        Products.append(myDict)
def add():
    ID=int(input("Pls Enter ID : "))
    Name=input("Pls Enter Name : ")
    Price=float(input("Pls Enter Price : "))
    Count=int(input("Pls Enter Count : "))
    Products.append({'id':ID , 'Name':Name , 'Price':Price , 'Count':Count })
    print("New Product Added Successfully")
def show_edit_menu():
    print("1-Edit Name")
    print("2-Edit Price")
    print("3-Edit Count")
    print("4-End Edit")
def edit():
    id=int(input("Pls Enter Product Id :" ))
    for i in range(len(Products)):
        if Products[i]['id']==id:
            while True:
                show_edit_menu()
                edit=int(input("Pls Choose from Edit Menu : "))
                if edit==1:
                    name=input("Pls Enter New Name : ")
                    Products[i]['Name']=name
                    print("Product Edited Successfully!")
                elif edit==2:
                    price=float(input("Pls Enter New Price : "))
                    Products[i]['Price']=price
                    print("Product Edited Successfully!")
                elif edit==3:
                    count=int(input("Pls Enter New Count : "))
                    Products[i]['Count']=count
                    print("Product Edited Successfully!")
                elif edit==4:
                    break
                else:
                    print("Value Error ,Try Again !")
def deletep():
    id=int(input("Pls Enter Product Id :" ))
    for i in range(len(Products)):
        if Products[i]['id']==id:
            Products.pop(i)
            print("Product Removed Successfully!")
            break
        else:
            print("Pls Enter a Valid Id ,See the Product List and Try Again Later !")
            break
def search():
    userKey=input("Pls Enter Product Id or Product Name:" )
    f=0
    for i in range(len(Products)):
        if str(Products[i]['id'])==userKey or (Products[i]['Name'].lower()==userKey.lower()) :
            print(Products[i])
            f=1
    if f==0:   
        print("Product Not Found!")
def buy():
    basket=[]
    while True:
        id=int(input("Pls Enter Product Id :" ))
        for i in range(len(Products)):
            if Products[i]['id']==id:
                print(f"We Have {Products[i]['Count']} of {Products[i]['Name']}")
                count=int(input("Pls Enter Count that You Want : "))

                if Products[i]['Count']>= count:
                    basket.append({'Name':Products[i]['Name'],
                    'Price':Products[i]['Price'],
                    'Count':count})
                    Products[i]['Count']-=count
                    print("Product Added to Basket Successfully!")
                else:
                    print("Product is Not Enough!")
                    print(f"You Can Buy just {Products[i]['Count']}")
        c=input("Do You Want To Continue? (Y/N)").lower()
        if c=="n":
            break
    total=0
    print('Name'+'\t'+'Price'+'\t'+'Count'+'\t'+'Total')
    for i in range(len(basket)):
        total+=basket[i]['Price']*basket[i]['Count']
        print(basket[i]['Name']+'\t'+str(basket[i]['Price'])+'\t'+str(basket[i]['Count'])+'\t'+str(basket[i]['Count']*basket[i]['Price']))
    print(f"Total Price : {total} \n Thanks!")
def saveAndExit():
    f=open('database.txt','w')
    for i in range(len(Products)):
        if i==len(Products)-1:
            row=str(Products[i]['id']) +','+Products[i]['Name']+','+str(Products[i]['Price'])+','+str(Products[i]['Count'])
        else:
            row=str(Products[i]['id']) +','+Products[i]['Name']+','+str(Products[i]['Price'])+','+str(Products[i]['Count'])+'\n'
        f.write(row)
    f.close()
    exit()
def Qrcode():
    id=int(input("Pls Enter Product Id :" ))
    for i in range(len(Products)):
            if Products[i]['id']==id:
                product='ID : '+str(+Products[i]['id']) +', Name : '+Products[i]['Name']+', Price : '+str(Products[i]['Price'])+', Count : '+str(Products[i]['Count'])
                img=qrcode.make(product)
                img.save("product.png")
f=Figlet(font="standard")
print(f.renderText("Welcome Store"))
load()
while True:
    show_menu()
    choice=int(input("Please choose a Number : "))
    if choice==1:
        add()
    elif choice==2:
        edit()
    elif choice==3:
        deletep()
    elif choice==4:
        search()
    elif choice==5:
        show_list()
    elif choice==6:
        buy()
    elif choice ==7:
        Qrcode()
    elif choice==8:
        saveAndExit()
        break
    else:
        print("Try Again!")