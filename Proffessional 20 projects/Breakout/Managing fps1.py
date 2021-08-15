# Simple program to show gravity and bounce with lateral movement
# Looking at inconsistent fps mac osx and windows
# Written in Mac os X and IDLE
# import time and then time.sleep(0.01) = 100fps to be adjusted to correct speed


import turtle
import time # to control game speed

win = turtle.Screen()
win.title('Gravity simulation - with side movement')
win.setup(850,600)
win.tracer(0)


ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')
ball.up()
ball.goto(-410,200)
ball.dy = 0
ball.dx = 1
ball.down()

ground = turtle.Turtle()
ground.shape('square')
ground.shapesize(0.5, 40)
ground.up()
ground.goto(0, -275)

gravity = 0.09
remaining_energy = 0.8 # increase for more bounce, decrease for less 


while True:
    win.update()

    ball.dy -= gravity   
    ball.goto(ball.xcor()+ball.dx, ball.ycor()+ball.dy)

    if ball.ycor() <= -260 and ball.dy<0:
        ball.dy *= -1
        ball.dy *= remaining_energy
        print(ball.dy)
        if ball.dy <0.5:
            ball.dy = 0
            gravity  = 0
            remaining_energy = 0

    if ball.xcor()>400:
        break
    
    # 0.01 = 100fps (10ms)
    # 0.0166 = 60fps(1/60) (16ms)
    # 0.0083 = 120 fps(1/120) (8ms)
    time.sleep(0.01)
        

    
        

        


