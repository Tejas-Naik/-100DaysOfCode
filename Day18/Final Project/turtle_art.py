import turtle as turtle_module
import random

art = turtle_module.Turtle()

color_list = ['#d4955f', '#d7503e', '#2f5e8e', '#e7da5c', '#94425b', '#161b28', '#9b493c', '#7aa7c3', '#28161d', 
              '#27130f', '#d14659', '#c08c9f', '#27835b', '#7db38d', '#4ba460', '#e5a9b7', '#0f1f16', '#333766',
              '#e9dc0c', '#9fb136', '#632c3f', '#23a4c4', '#eaaba2', '#692c27', '#a4d1bb', '#97cedc']

screen = turtle_module.Screen()

# setting the speed of the turtle
art.speed('fastest')
# this is setting the heading from 0 to 360
art.setheading(225)
# penup will not drawn 
art.penup()
# hiding the arrow of turtle
art.hideturtle()
art.fd(250)
art.setheading(0)

def something():
        
    for _ in range(10):
        art.dot(20, random.choice(color_list))
        art.penup()
        art.fd(50)
        art.pendown()

    art.setheading(90)
    art.penup()
    art.forward(50)
    art.setheading(180)
    art.forward(500)
    art.setheading(360)

for i in range(10):
    something()


screen.exitonclick()
