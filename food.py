from turtle import *
from random import *


class Food(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.color("purple")
        self.shapesize(0.5, 0.5, 0.5)
        self.speed("fastest")
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.goto(rand_x, rand_y)

    def refresh(self):
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.goto(rand_x, rand_y)
