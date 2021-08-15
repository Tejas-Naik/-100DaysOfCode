# to create a car object from a CarBlueprint() class
# car = CarBlueprint()
from turtle import Turtle, Screen

timmy = Turtle()                # creating a turtle object
print(timmy)
timmy.speed(100)
my_screen = Screen()            # creating a screen object
print(my_screen.canvheight)     # checking the height of the canvas of Screen
print(my_screen.canvwidth)      # checking the width of the canvas of Screen

# changing the shape of the timmy(turtle)
timmy.shape("turtle")
for i in range(50):
    timmy.forward(20 + i)
    timmy.backward(20 + i)

    timmy.left(90)
    timmy.forward(5)
    timmy.right(90)
for i in range(50):
    timmy.right(180)
    timmy.forward(20 + i)
    timmy.backward(20 + i)

    timmy.left(90)
    timmy.forward(5)
    timmy.left(90)


# making the graphics screen exit on click
my_screen.exitonclick()
