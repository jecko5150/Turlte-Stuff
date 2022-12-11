import turtle
from turtle import Turtle
import time

score = 0


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.ht()
        self.color('white')
        self.setpos(220.00, 270.00)
        self.write(f'Score: {self.score}', align='center', font=("courier", 18, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=("courier", 18, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'GAME OVER\nScore: {self.score}', align="center", font=('courier', 18, 'normal'))


class Countdown(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.color('white')
        self.goto(0, 0)
        self.start_game()

    def start_game(self):
        x = 3
        for _ in range(3):
            self.write(f'{x}', align="center", font=('courier', 36, 'bold'))
            time.sleep(1)
            self.clear()
            x -= 1
        self.write(f'GAME ON!', align="center", font=('courier', 36, 'bold'))
        time.sleep(1)
        self.clear()

    def replay(self):
        self.clear()
        self.write("PLAY AGAIN??", align="center", font=('courier', 36, 'bold'))



class PlayerName(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.color('white')
        self.setpos(-210, 270)
        name = turtle.textinput("", "Enter Player Name")
        self.write(f"Player: {name}", align="center", font=('courier', 18, 'normal'))


