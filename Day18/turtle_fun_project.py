from turtle import Turtle, Screen
import random

timmy = Turtle()

screen = Screen()
# changing the shape of turtle
timmy.shape('turtle')
timmy.color('blue')

# drawing square
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)


for i in range(20):
    timmy.forward(15)
    timmy.penup()
    timmy.forward(15)
    timmy.pendown()



tom = Turtle()


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tom.forward(100)
        tom.right(angle)

colours = ['SlateGray', 'SeaGreen', 'IndianRed', 'DarkOrchid', 'CornflowerBlue', 'wheat', 'lightseagreen']

for i in range(3, 11):
    tom.color(random.choice(colours))
    draw_shape(i)

# challenge 4
betty = Turtle()
moves = [betty.forward(100), betty.right(90), betty.left(100), betty.backward(100)]

for i in range(10):
    random.choice(moves)

screen.exitonclick()
