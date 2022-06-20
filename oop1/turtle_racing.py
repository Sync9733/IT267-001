#create object
from random import randint
from turtle import Turtle

#create object
leo = Turtle ('turtle')
leo.color('blue')
leo.penup()
leo.goto(-160,100)
leo.pendown()

dona = Turtle('turtle')
dona.color('purple')
dona.penup()
dona.goto(-160,70)
dona.pendown()

Raphael = Turtle('turtle')
Raphael.color('Red')
Raphael.penup()
Raphael.goto(-160,40)
Raphael.pendown()

Michaelangelo = Turtle('turtle')
Michaelangelo.color('Orange')
Michaelangelo.penup()
Michaelangelo.goto(-160,10)
Michaelangelo.pendown()

for move in range(100):
    leo.forward(randint(1,5))
    dona.forward(randint(1,5))
    Raphael.forward(randint(1,5))
    Michaelangelo.forward(randint(1,5))
