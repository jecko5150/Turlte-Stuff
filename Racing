import random
import turtle
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput('Make your bet', 'Which turtle will win?')
print(user_bet)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
racers = []

y = 100
for color in colors:
    racer = Turtle()
    racer.color(color)
    racer.penup()
    racer.goto(-200, y)
    racers.append(racer)
    y -= 30

if user_bet:
    is_race_on = True

while is_race_on:
    for racer in racers:
        racer.fd(random.randint(1, 10))
        if racer.xcor() > 249:
            is_race_on = False
            winning_color = racer.pencolor()
            if winning_color == user_bet:
                print(f'{winning_color.title()} won! You win too!')
            else:
                print(f'{winning_color.title()} won, you lose....')

screen.exitonclick()
