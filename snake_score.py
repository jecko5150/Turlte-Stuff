from turtle import Turtle

score = 0


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.ht()
        self.color('white')
        self.setpos(0.00, 280.00)
        self.write(f'Score: {self.score}', align='center', font=("courier", 12, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=("courier", 12, 'normal'))

    def game_over(self):
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=("courier", 12, 'normal'))
        self.write(f'GAME OVER', align="center", font=('courier', 12, 'normal'))
