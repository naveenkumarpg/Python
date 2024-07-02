import random
from turtle import Turtle, Screen

turtle = Turtle()
my_screen = Screen()
my_screen.colormode(255)

turtle.pensize(15)
turtle.speed(2)
directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_shape():
    for _ in range(300):
        turtle.pencolor(random_color())
        turtle.right(random.choice(directions))
        turtle.forward(30)


draw_shape()
my_screen.exitonclick()
