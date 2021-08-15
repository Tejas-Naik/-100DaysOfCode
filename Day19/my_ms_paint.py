from turtle import Turtle, Screen

pen = Turtle()

screen = Screen()

pen.penup()
pen.setx(-300)
pen.sety(100)
pen.pendown()

# to listen fro the user for input we use the listen method

def home_():
    pen.penup()
    pen.home()
    pen.setx(-300)
    pen.sety(100)
    pen.pendown()

def move_forwards():
    pen.fd(20)


def move_backwards():
    pen.backward(20)


def turn_left():
    # pen.left(90)
    new_heading = pen.heading()+10
    pen.setheading(new_heading)

def turn_right():
    # pen.right(90)
    new_heading = pen.heading()-10
    pen.setheading(new_heading)

def degree45():
    new_heading = pen.heading()+45
    pen.setheading(new_heading)

def clear():
    pen.clear()
    home_()

screen.listen()
screen.onkey(key='Up', fun=move_forwards)
screen.onkey(key='Down', fun=move_backwards)
screen.onkey(key='Right', fun=turn_right)
screen.onkey(key='Left', fun=turn_left)
screen.onkey(key='f', fun=degree45)
screen.onkey(key='c', fun=clear)


screen.exitonclick()
