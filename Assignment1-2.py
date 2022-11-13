while True:
    try:
        a=float(input("Please enter the 1st side of the triangle:"))
        b=float(input("Please enter the 2ed side of the triangle:"))
        c=float(input("Please enter the 3th side of the triangle:"))
    except:
        print("PLS Enter a Valid Number")
        continue

    if a+b>c and a+c>b and b+c>a:
        print("this can be triangle")
    else:
        print("this can NOT be triangle")

    q=input("Do u Want to Continue?Y/N")
    q=q.lower()
    if q=="y":
        continue
    elif q=="n":
        break
    else:
        print("sth went wrong!pls try again!")
        break