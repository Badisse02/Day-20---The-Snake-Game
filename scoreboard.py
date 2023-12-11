from turtle import *


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as d:
            self.high_score = int(d.read())
        self.hideturtle()
        self.color("White")
        self.penup()
        self.goto(0, 270)
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", ('Arial', 20, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as d:
                d.write(f"{self.high_score}")
        self.score = 0
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ('Arial', 25, 'normal'))
