from turtle import *


class Snake:

    def __init__(self):
        start_x = 0
        self.snake = []
        for i in range(3):
            self.snake.append(Turtle("square"))
            self.snake[i].color("white")
            self.snake[i].penup()
            self.snake[i].setx(start_x)
            start_x -= 20
        self.head = self.snake[0]

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.snake[0].forward(15)

    def reset_snake(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        start_x = 0
        for i in range(3):
            self.snake.append(Turtle("square"))
            self.snake[i].color("white")
            self.snake[i].penup()
            self.snake[i].setx(start_x)
            start_x -= 20
        self.head = self.snake[0]

    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def growth_length(self):
        new_x = self.snake[-1].xcor()
        new_y = self.snake[-1].ycor()
        self.snake.append(Turtle("square"))
        self.snake[-1].color("white")
        self.snake[-1].penup()
        self.snake[-1].goto(new_x, new_y)
