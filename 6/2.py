import turtle
from math import sin , pi

skk = turtle.Pen()
skk.shape("turtle")

angle0 = 30
i = 3
n = 20
skk.penup()
skk.goto(n,0)
skk.pendown()
skk.left(angle0)

while i <= n:
    for j in range(i):
        skk.left(180-(180*(i-2)/i))
        angle = 90-(angle0)
        skk.forward(2*n*(i-2)*sin(angle/180*pi))

    skk.right(angle0)
    skk.penup() 
    skk.goto(n*(i-1), 0)
    skk.pendown()
    i = i+1

    angle0 = (180*(i-2)/i)/2
    skk.left(angle0)

turtle.done()