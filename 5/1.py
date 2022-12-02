def box():
    n=int(input("n = "))
    m=int(input("m = "))

    for j in range (m):
        if j%2==0:
            for i in range(n):
                if i%2==0:
                    print('#',end="")
                else:
                    print('*',end="") 
            print()
        else:
            for i in range(n):
                if i%2==0:
                    print('*',end="")
                else:
                    print('#',end="") 
            print()
box()