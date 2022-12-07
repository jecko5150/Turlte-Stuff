import turtle as s
from random import randint

co = []

for r in range(-800, 800):
    co.append(r)


def stars():
    q = co[randint(-700, 700)]
    w = co[randint(-700, 700)]
    star = s.Turtle()
    star.hideturtle()
    star.shapesize(.05, .05)
    star.color('white')
    star.penup()
    star.shape('circle')
    star.speed(500)
    star.setposition(w, q)
    star.pendown()
    star.showturtle()
    star.circle(0)
