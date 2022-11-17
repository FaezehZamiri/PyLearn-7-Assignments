h=float(input("Pls Enter Hour: "))
m=float(input("Pls Enter Minute: "))
s=float(input("Pls Enter Second: "))
if s>60:
    s=s-60
    m=m+1
if m>60:
    m=m-60
    h=h+1
if h>12:
    h=h-12

time=h*3600+m*60+s

print(f"{h} : {m} : {s} equal {time} second")