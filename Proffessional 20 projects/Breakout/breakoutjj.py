# Very simple breakout game J Jouber 22 Oct 2019
# Speed may need adjustment on windows
# Written in osX and IDLE
# This code can be copied, changed, updated and if improved - Please let me know how!!

import turtle
import random
#import time # and time.sleep(0.017) windows

win = turtle.Screen()
win.setup(width=800, height=600)
win.bgcolor('black')
win.tracer(0)
win.title('Breakout Game')

paddle = turtle.Turtle()
paddle.shape('square')
paddle.shapesize(1, 5) # Turtle still facing right, stretching y axis for turtle!!
paddle.color('white')
paddle.up()
paddle.goto(0, -270)

ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.up()
ball.dx = random.choice((-5, -4, 4, 5)) # May need change in windows eg 0.03, etc
ball.dy = random.choice((-6, -5, -4, 4, 5, 6))

pen = turtle.Turtle()
pen.color('red')
pen.up()
pen.hideturtle()
pen.goto(250,-220)
pen.write('Score: 0', align='center', font=('Courier', 24, 'normal'))

colors = ['red', 'blue', 'green', 'cyan', 'purple', 'yellow', 'orange']
score = 0

def paddle_right():
    if paddle.xcor()<350:
        paddle.setx(paddle.xcor()+80)


def paddle_left():
    if paddle.xcor()>-350:
        paddle.setx(paddle.xcor()-80)


def border_check():
    if ball.ycor()>280:
        ball.dy *= -1
    if ball.xcor()>380 or ball.xcor()<-380:
        ball.dx *= -1

def paddle_check():
    if ball.ycor() <= -250 and ball.ycor() >=-260 and ball.dy<0:
        if ball.xcor()-10 <= paddle.xcor() + 50 and ball.xcor() +10 >= paddle.xcor()-50:
            ball.dy *= -1


win.listen()
win.onkey(paddle_right, 'Right')
win.onkey(paddle_left, 'Left')

# Want to place blocks at these coordinates:
x_list = [-340, -230, -120, -10, 100, 210, 320]
y_list = [280, 255, 230, 205, 180]
block_list = []

for i in y_list:
    for j in x_list:
        block = turtle.Turtle()
        block.shape('square')
        block.shapesize(stretch_len=5, stretch_wid=1)
        block.color(random.choice(colors))
        block.up()
        block.goto(j,i)
        block_list.append(block)
    
block_count = len(block_list)

while block_count > 0:
    
    #time.sleep(0.017) # windows?
    
    win.update()
    ball.goto(ball.xcor()+ball.dx, ball.ycor()+ball.dy)
    border_check()
    paddle_check()
    #paddle.setx(ball.xcor()) # Autopilot
    
    if ball.ycor() <-280:
        ball.goto(0,0)
        ball.dx *= -1
        if score>0:
            score -= 1
        pen.clear()
        pen.write(f'Score: {score}', align='center', font=('Courier', 24, 'normal'))
        
    # Block collisions:
    for i in block_list:
        if ball.xcor()+10 >= i.xcor()-60 and ball.xcor()-10 <= i.xcor()+60:
            if ball.ycor() >= i.ycor()-20 and ball.ycor() <= i.ycor()+20:
                ball.dy *= -1
                i.goto(1000,1000)
                score += 1
                block_count -= 1
                pen.clear()
                pen.write(f'Score: {score}', align='center', font=('Courier', 24, 'normal'))

# Game Over
pen.clear()
pen.goto(0,0)
pen.write(f'GAME OVER\nScore: {score}', align='center', font=('Courier', 40, 'normal'))
