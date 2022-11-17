time=float(input("Pls Enter Time in Second: "))

h=int(time//3600)
m=int((time-h*3600)/60)
s=float(time-h*3600-m*60)

print(f"{time} second equal {h} : {m} : {s}")