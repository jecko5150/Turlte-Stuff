import turtle
from planets import stars
from math import *



# create the screen

screen = turtle.Screen()
screen.screensize(1500, 1000)
screen.bgcolor('midnight blue')
screen.tracer(0)
screen.title("Solar System")

# turtle object for sun
sun = turtle.Turtle()
planet_list = []
# Turn on stars
for r in range(100):
    stars()

# shape of sun
sun.shape('circle')
sun.shapesize(4)

# color of sun
sun.color('gold')


class Planet(turtle.Turtle):
    def __init__(self, name, radius, color, size):
        super().__init__(shape='circle')
        self.name = name
        self.radius = radius
        self.c = color
        self.size = size
        self.shapesize(self.size)
        self.color(self.c)
        self.angle = 0
        self.penup()

    def move(self):
        # Angle in radians
        x = self.radius * cos(self.angle)
        y = self.radius * sin(self.angle)
        self.goto(sun.xcor() + x, sun.ycor() + y)

mercury = Planet("Mercury", 75, 'grey', .085)
venus = Planet("Venus", 100, 'orange', .089)
earth = Planet("Earth", 125, 'lime green', .090)
mars = Planet("Mars", 190, 'red', .064)
jupiter = Planet("Jupiter", 225, 'navajo white', .545)
saturn = Planet("Saturn", 292, 'pink', .460)
uranus = Planet("Uranus", 313, 'medium purple', .226)
neptune = Planet("Neptune", 350, 'steel blue', .220)

# adding planets to a list
myList = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

for x in range(len(myList)):
    a = myList[x].name
    planet_list.append(a)


def label(u, v):
    u.write(v, True, font=('Arial', 10, 'normal'))




while True:
    new_angle = []
    screen.update()
    r = turtle.Turtle()
    r.hideturtle()
    r.penup()
    r.speed(500)



    for i in myList:

        i.move()

    for x in myList:
        r.setpos(x.radius * cos(x.angle), x.radius * sin(x.angle))
        r.color(x.pencolor())
        label(r, x.name)

    mercury.angle += 0.05
    venus.angle += 0.03
    earth.angle += 0.01
    mars.angle += 0.007
    jupiter.angle += 0.02
    saturn.angle += 0.018
    uranus.angle += 0.016
    neptune.angle += 0.005
    r.clear()






