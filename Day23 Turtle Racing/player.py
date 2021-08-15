from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.starting_position()

    def goup(self):
        self.forward(MOVE_DISTANCE)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        self.backward(MOVE_DISTANCE)

    def go_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)
        self.setheading(90)

    def go_right(self):
        self.setheading(360)
        self.forward(MOVE_DISTANCE)
        self.setheading(90)

    def starting_position(self):
        self.goto(STARTING_POSITION)

    def has_finished(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
