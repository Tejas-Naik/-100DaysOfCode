from turtle import Turtle, Screen
import random

mik = Turtle()
mik.speed('fastest')
screen = Screen()

colours = ['skyblue', 'red']

for i in range(74):
    mik.color(random.choice(colours))
    mik.circle(100)
    mik.left(5)

screen.exitonclick()
