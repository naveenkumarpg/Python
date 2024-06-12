import random
from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        pen.color(c)
        pen.forward(steps)
        pen.right(30)

screen.exitonclick()
