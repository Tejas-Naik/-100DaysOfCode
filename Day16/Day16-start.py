from turtle import Turtle, Screen

screen = Screen()
screen.canvheight = 400
screen.canvwidth = 400

timmy = Turtle()
timmy.shape("turtle")

timmy.color("red")
timmy.forward(100)      # 100 pixels to move forward
timmy.right(90)         # 90 degrees to turn right
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
screen.exitonclick()

"""
car = Class()
Class = class is a blueprint for creating objects
Attributes = variables associated to the class eg(car.name)
Methods = actions that can be done using that class eg(car.move())
"""
