# Simple program to show gravity and bounce with lateral movement
# Looking at inconsistent fps between mac os x and windows
# Written in osX and IDLE
# Using win.ontimer(function_name(), ms) 10ms = 100fps


import turtle


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


def update_game():
    global gravity, remaining_energy
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

    

while True:
    # 10ms = 100fps(1/100)
    # 16ms = 60fps(1/60)
    # 88ms = 120 fps(1/120)
    win.ontimer(update_game(), 8) # 8ms - control game speed
    
    if ball.xcor()>400:
        break 

    
        

        


