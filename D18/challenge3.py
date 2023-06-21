#drawing a triangle,hexagon.......etc

import turtle as t
from turtle import Screen
import random


tim = t.Turtle()

colours = ["red","dark salmon","medium purple","royal blue","orange red","light coral","maroon","navy"]


def draw_shape(num_sides):
    angle = 360/ num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)















screen = Screen()
screen.exitonclick()