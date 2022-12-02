n = int(input("Please Enter An Integer Number : "))

def Shape(n):
    for i in range(1,2*n+1,2):
        x = (2*n+1-i)//2
        print(' '*x+'*'*i)

    for i in range(2*n-3,0,-2):
        x = (2*n+1-i)//2
        print(' '*x+'*'*i)

Shape(n)