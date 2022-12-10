from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.hideturtle()


def move_forward():
    tim.forward(5)


def north():
    tim.seth(90)
    screen.onkeypress(move_forward)


def south():
    tim.seth(270)
    screen.onkeypress(move_forward)


def east():
    new_heading = tim.heading() - 20
    tim.seth(new_heading)
    screen.onkeypress(move_forward)


def west():
    new_heading = tim.heading() + 20
    tim.seth(new_heading)
    screen.onkeypress(move_forward)


def clear():
    screen.onkey(fun=tim.clear, key='c')
    tim.home()


def direction():
    tim.speed('fastest')
    screen.listen()
    screen.onkey(key="space", fun=move_forward)
    screen.onkey(key='Up', fun=north)
    screen.onkey(key='Down', fun=south)
    screen.onkey(key='Left', fun=west)
    screen.onkey(key='Right', fun=east)
    clear()


direction()

screen.exitonclick()
