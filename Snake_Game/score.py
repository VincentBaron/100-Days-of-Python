from turtle import *

FONT = ("Arial", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.refresh_score()


    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.points}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)

    def update(self):
        self.points += 1
        self.refresh_score()
