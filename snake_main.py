import time
from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Snakes!!!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    snake.boundaries()

    #     Detect food with snake
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()

#         Detect Wall


screen.exitonclick()
