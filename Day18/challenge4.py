from turtle import Turtle, Screen
import random

betty = Turtle()

colours = ['SlateGray', 'SeaGreen', 'IndianRed',
           'DarkOrchid', 'CornflowerBlue', 'DeepSkyBlue', 'lightseagreen',
           'black', 'darkblue', 'gray0', ]

colours = ['black', 'red', 'blue', 'green']


screen = Screen()
# making the turtles nib bigger
betty.pensize(10)
betty.speed("fastest")


moves = [90, 180, 270, 0]

for _ in range(500):
    betty.color(random.choice(colours))
    # betty.pencolor(colour())
    betty.forward(30)
    betty.setheading(random.choice(moves))

screen.exitonclick()
