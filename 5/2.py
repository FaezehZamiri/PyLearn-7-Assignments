def table():
    n=int(input("n = "))
    m=int(input("m = "))
    for i in range(1,n+1):
        for j in range(1,m+1):
            print(format(i*j,'5d'),end='')
        print()

table()