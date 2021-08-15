from turtle import Turtle
import random

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-140, 250)
        self.write(f"Level: {self.level}", align="right", font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="right", font=FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)
