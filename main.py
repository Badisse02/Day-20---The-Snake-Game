import time
from snake import *
from food import *
from scoreboard import *


s = Screen()
s.setup(600, 600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)
sb = Scoreboard()


# def new_square(l):
#     a = len(l)
#     pos_x = l[a - 1].xcor()
#     pos_y = l[a - 1].ycor()
#


sn = Snake()
food = Food()
s.listen()
s.onkey(key="Up", fun=sn.up)
s.onkey(key="Down", fun=sn.down)
s.onkey(key="Left", fun=sn.left)
s.onkey(key="Right", fun=sn.right)

games_is_on = True
while games_is_on:
    s.update()
    time.sleep(0.1)
    sn.move()

    if sn.head.distance(food) < 15:
        food.refresh()
        sb.score += 1
        sb.print_score()
        sn.growth_length()
    if sn.head.xcor() > 280 or sn.head.xcor() < -280 or sn.head.ycor() > 280 or sn.head.ycor() < -280:
        sb.reset()
        sn.reset_snake()
    for seg in sn.snake[1:]:
        if seg.distance(sn.head) < 5:
            sb.reset()
            sn.reset_snake()

s.exitonclick()
