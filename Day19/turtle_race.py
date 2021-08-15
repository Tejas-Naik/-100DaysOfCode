from turtle import Turtle, Screen
import random


screen = Screen()
is_race_on = False
# there is a function called setup() which sets the screen's dimentions
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    "Choose Colour", "on which turtle do you bet? enter the color:")
colours = ['blue', 'indigo', 'green', 'yellow', 'orange', 'red']
y_pos = [-70, -40, -10, 20, 50, 80]

all_turtles = []

for i in range(6):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(colours[i])
    new_turtle.goto((-230, y_pos[i]))
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print("You won!!")
            else:
                print(f"Sorry you lost, the winner is {winner}")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
