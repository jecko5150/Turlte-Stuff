import time
from turtle import Screen

from scoreboard import Scoreboard, Countdown, PlayerName
from snake import Snake
from food import Food

game_is_on = True

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Snakes!!!")
screen.tracer(0)

snake = Snake()
food = Food()
player = PlayerName()
countdown = Countdown()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="1", fun=screen.resetscreen)


while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    #     Detect food with snake
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.add_snake()

    #         Detect Wall
    if snake.head.xcor() > 290:
        game_is_on = False
        scoreboard.game_over()
    elif snake.head.ycor() > 290:
        game_is_on = False
        scoreboard.game_over()
    elif snake.head.xcor() < -290:
        game_is_on = False
        scoreboard.game_over()
    elif snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    #     Detect Snake Body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.mainloop()
