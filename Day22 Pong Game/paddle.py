from turtle import Turtle
from ball import Ball

ball = Ball()
speed = ball.move_speed

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.create_paddle()

    def create_paddle(self):
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.position)

    def go_up(self):
        if speed == 0.096059601:
            new_y = self.ycor() + 35
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def go_down(self):
        if speed == 0.096059601:
            new_y = self.ycor() - 35
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
