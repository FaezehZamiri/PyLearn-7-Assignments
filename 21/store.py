import sqlite3
from pyfiglet import Figlet
import qrcode
import pandas as pd

con = sqlite3.connect("digikala.db")
cur = con.cursor()
df = pd.DataFrame(columns=["ID","Name","Price","Count"])

def show_menu():
    print("1-Add Product")
    print("2-Edit Product")
    print("3-Delete Product")
    print("4-Search")
    print("5-Show List")
    print("6-Buy")
    print("7-Make QRCode")
    print("8-Exit")

def load():
    global df
    df = pd.DataFrame(columns=["ID","Name","Price","Count"])
    for row in cur.execute("SELECT * FROM Products"):
        df.loc[len(df)] = list(row)
    
def show_list():
    print(df.set_index('ID'))

def add():
    ID=int(input("Pls Enter ID : "))
    Name=input("Pls Enter Name : ")
    Price=float(input("Pls Enter Price : "))
    Count=int(input("Pls Enter Count : "))
    cur.execute(f"INSERT INTO Products(ID,Name,Price,Count) VALUES({ID},'{Name}',{Price},{Count})")
    con.commit()
    load()
    print("New Product Added Successfully")

def show_edit_menu():
    print("1-Edit Name")
    print("2-Edit Price")
    print("3-Edit Count")
    print("4-End Edit")

def edit():
    id=int(input("Pls Enter Product Id :" ))
    while True:
        show_edit_menu()
        edit=int(input("Pls Choose from Edit Menu : "))
        if edit==1:
            name=input("Pls Enter New Name : ")
            cur.execute(f"UPDATE Products SET Name = {name} WHERE ID = {id}")
            con.commit()
            load()
            print("Product Edited Successfully!")
        elif edit==2:
            price=float(input("Pls Enter New Price : "))
            cur.execute(f"UPDATE Products SET Price = {price} WHERE ID = {id}")
            con.commit()
            load()
            print("Product Edited Successfully!")
        elif edit==3:
            count=int(input("Pls Enter New Count : "))
            cur.execute(f"UPDATE Products SET Count = {count} WHERE ID = {id}")
            con.commit()
            load()
            print("Product Edited Successfully!")
        elif edit==4:
            break
        else:
            print("Value Error ,Try Again !")

def delete():
    id=int(input("Pls Enter Product Id :" ))
    cur.execute(f"DELETE FROM Products WHERE ID = {id}")
    con.commit()
    print("Product Removed Successfully!")
    load()

def search():
    global df
    userKey=input("Pls Enter Product Id or Product Name:" )
    f = 0
    for index, row in df.iterrows():
        if row['Name'] == userKey or str(row['ID']) == userKey:
            f = 1
            print(row)
    if f == 0:   
        print("Product Not Found!")

def buy():
    basket=pd.DataFrame(columns=["ID","Name","Price","Count"])
    while True:
        id=int(input("Pls Enter Product Id :" ))
        for index, row in df.iterrows():
            if row['ID'] == id:
                print(f"We Have {row['Count']} of {row['Name']}")
                count=int(input("Pls Enter Count that You Want : "))

                if row['Count']>= count:
                    product = {'ID':len(basket)+1,
                    'Name':row['Name'],
                    'Price':row['Price'],
                    'Count':count}
                    basket.loc[len(basket)] = product

                    cur.execute(f"UPDATE Products SET Count = {row['Count']-count} WHERE ID = {id}")
                    con.commit()
                    load()
                    print("Product Added to Basket Successfully!")

                else:
                    print("Product is Not Enough!")
                    print(f"You Can Buy just {row['Count']}")

        c=input("Do You Want To Continue? (Y/N)").lower()
        if c=="n":
            break
    total=0
    print(basket.set_index('ID'))
    for index, row in basket.iterrows():
        total+=row['Price']*row['Count']

    print(f"Total Price : {total} \n Thanks!")

def Qrcode():
    id=int(input("Pls Enter Product Id :" ))
    for index, row in df.iterrows():
            if row['ID'] == id:
                product=f"ID : {row['ID']} , Name : {row['Name']}, Price : {row['Price']}, Count : {row['Count']}"
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
        delete()
    elif choice==4:
        search()
    elif choice==5:
        show_list()
    elif choice==6:
        buy()
    elif choice ==7:
        Qrcode()
    elif choice==8:
        break
    else:
        print("Try Again!")
