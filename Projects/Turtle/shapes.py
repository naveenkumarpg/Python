import random
from turtle import Turtle, Screen

turtle = Turtle()
colors = ['Red', 'Green', 'Blue', 'Cyan', 'Magenta', 'Black', 'Gray', 'Silver', 'Maroon', 'Olive',
          'Navy', 'Purple', 'Teal', 'Lime', 'Fuchsia', 'Aqua', 'Orange', 'Pink']


def draw_shape(number_of_sides):
    angle = 360 / number_of_sides

    for _ in range(number_of_sides):
        turtle.forward(100)
        turtle.pencolor(random.choice(colors))
        turtle.right(angle)


for sides in range(3, 15):
    draw_shape(sides)

my_screen = Screen()
my_screen.exitonclick()
