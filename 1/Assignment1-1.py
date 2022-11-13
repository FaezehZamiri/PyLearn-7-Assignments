import math

while True:
    op=input("Pls Select Operation or Enter Number of Operation :\n 1. +  \n 2. -  \n 3. *  \n 4. / \n 5. Sqrt \n 6. Sin \n 7. Cos \n 8. Tan \n 9. Cot \n 10. Fatorial")
    op=op.lower()

    if op == '+' or op == '-' or op == '*' or op =='/' or op == "1" or  op == '2' or op == '3' or op =='4':
        try:
            a=float(input("Pls Enter the First Number: "))
            b=float(input("Pls Enter thr Secend Number: "))
        except:
            print("PLS Enter a Valid Number")
            continue
    elif op == 'sin' or op == 'cos' or op == 'sqrt' or op =='tan' or op == "cot" or  op == '5' or op == '6' or op =='7' or op =='8' or op =='9' :
        try:
            a=float(input("PLS Enter Angle in Degree"))
        except:
            print("PLS Enter a Valid Number")
            continue
    elif op == 'factorial' or op == '10':
        try:
            a=int(input("Pls Enter the Number: "))
        except:
            print('the Number Should be Integer')
            continue
    else:
        print("sth went wrong!pls try again!")
        continue



    if op=="1" or op=="+" :
        result=a+b
        print(f"{a}+{b}={result}")
    elif  op=="2" or op=="-" :
        result=a-b
        print(f"{a}-{b}={result}")
    elif op=="3" or op=="*" :
        result=a*b
        print(f"{a}*{b}={result}")
    elif op=="4" or op=="/" :
        if b==0:
            print("Number can not dvide zero")
        else:
            result=a/b
            print(f"{a}/{b}={result}")
    elif op=="5" or op=="sqrt":
        if a<0:
            print("Number can not be negative")
        else:
            aa=a**(0.5)
            print(f"{a}**0.5={aa}")
    elif op=="6" or op=="sin" :
        c=a*math.pi/180
        aa=math.sin(c)
        print(f"{a} degree equal {c} Radian & Sin({a})= {aa}")
    elif op=="7" or op=="cos" :
        c=a*math.pi/180
        aa=math.cos(c)
        print(f"{a} degree equal {c} Radian & Cos({a})={aa}")
    elif op=="8" or op=="tan" :
        c=a*math.pi/180
        aa=math.tan(c)
        print(f"{a} degree equal {c} Radian & Tan({a})={aa}")
    elif op=="9" or op=="cot" :
        c=a*math.pi/180
        aa=math.cos(c)/math.sin(c)
        print(f"{a} degree equal {c} Radian & Cot({a})={aa}")
    elif op=="10" or op=="factorial":
        aa=math.factorial(a)
        print(f"the factorial of {a} is {aa}")
    else:
        print("sth went wrong!pls try again!")
        
    
    q=input("Do u Want to Continue?Y/N")
    q=q.lower()
    if q=="y":
        continue
    elif q=="n":
        break
    else:
        print("sth went wrong!pls try again!")
        break
