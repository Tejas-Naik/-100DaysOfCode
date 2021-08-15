# Breakout using Python 3 with Turtle and classes
# J Joubert 28 Oct 2019
# Written in osX and IDLE
# This code can be copied, changed, updated and if improved - Please let me know how!!

import turtle
import random
#import time # and time.sleep(0.017) windows

win = turtle.Screen()
win.setup(800,600)
win.bgcolor('black')
win.title('Simple breakout with Python 3 and Turtle with classes')
win.tracer(0)
win.listen()

class Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.shapesize(1,5)
        self.up()
        self.color('white')
        self.goto(0,-250)

    def move_right(self):
        if self.xcor() <= 350:
            self.goto(self.xcor()+60, self.ycor())

    def move_left(self):
        if self.xcor() >= -350:
            self.goto(self.xcor()-60, self.ycor())


class Ball(turtle.Turtle):
    def __init__(self, paddle, block_list):
        super().__init__(shape='circle')
        self.up()
        self.color('white')
        self.dx, self.dy = 5, 6
        self.paddle = paddle
        self.block_list = block_list

    def move(self):
        self.goto(self.xcor()+self.dx, self.ycor()+self.dy)

        # Border bounce
        if self.xcor() <= -380 or self.xcor() >=380:
            self.dx *= -1
        if self.ycor() >= 280:
            self.dy *= -1
        if self.ycor() < -300:
            self.goto(0,0)
            
        # Paddle bounce
        if (-240 <= self.ycor() <= -230) and (paddle.xcor()-60 < self.xcor() < paddle.xcor()+60) and self.dy<0:
            self.dy *= -1

        # Block collision check
        for i in block_list:
            if (i.ycor()-20 <= self.ycor() <= i.ycor()+20) and (i.xcor()-60 < self.xcor()<i.xcor()+60) and ball.dy>0:
                i.goto(1000,1000)
                ball.dy *= -1
                block_list.remove(i)
        

class Block(turtle.Turtle):
    def __init__(self, xpos, ypos):
        super().__init__(shape='square')
        self.up()
        self.colors = ['red', 'blue', 'green', 'cyan', 'yellow', 'orange', 'purple']
        self.shapesize(1,5)
        self.goto(xpos, ypos)
        self.color(random.choice(self.colors))
        
      
        
x_list = [-340, -230, -120, -10, 100, 210, 320]
y_list = [280, 255, 230, 205, 180]
block_list = []

paddle = Paddle()
ball = Ball(paddle, block_list)

for i in x_list:
    for j in y_list:
        block = Block(i,j)
        block_list.append(block)


game_over = False

win.onkey(paddle.move_right, 'Right')
win.onkey(paddle.move_left, 'Left')


while len(block_list)>0:
    try:
        win.update()
        ball.move()
        #time.sleep(0.017) # windows?
    except:
        print('Exit Game')
        break

