from turtle import Turtle
from time import sleep


class Messenger(Turtle):
    def __init__(self, fontcolor, fontsize, fonttype):
        """Turtle Class to enable writing messages to the screen"""
        super(Messenger, self).__init__()
        self.pu()
        self.hideturtle()
        self.setposition(0, 0)
        self.pencolor(fontcolor)
        self.font = ("Comic Sans", fontsize, fonttype)

    def message_time(self, message, time):
        """Displays message for the given time.
        Previous message are cleared, which allows messages to be written to the same location on screen.
        If time <= 0 then the message is not cleared until the next message is written."""
        self.clear()  # Clear any previous message
        self.write(arg=message, move=False, align="center", font=self.font)
        if time > 0:
            sleep(time)
            self.clear()

    def message_position(self, message, position):
        """Displays message at the given position.
        Previous messages are NOT cleared."""
        self.setposition(position)
        self.write(arg=message, move=False, align="center", font=self.font)
