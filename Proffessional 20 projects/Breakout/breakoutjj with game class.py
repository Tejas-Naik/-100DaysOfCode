# Breakout using Python 3 with Turtle and classes
# J Joubert 28 Oct 2019
# Written in osX and IDLE
# This code can be copied, changed, updated and if improved - Please let me know how!!

import turtle
import random
#import time # and time.sleep(0.017) windows



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
        if (-240 <= self.ycor() <= -230) and (self.paddle.xcor()-60 < self.xcor() < self.paddle.xcor()+60) and self.dy<0:
            self.dy *= -1

        
        

class Block(turtle.Turtle):
    def __init__(self, xpos, ypos):
        super().__init__(shape='square')
        self.up()
        self.colors = ['red', 'blue', 'green', 'cyan', 'yellow', 'orange', 'purple']
        self.shapesize(1,5)
        self.goto(xpos, ypos)
        self.color(random.choice(self.colors))


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.color('red')
        self.up()
        self.hideturtle()
        self.goto(200,-200)


class Game():
    def __init__(self):
        self.win = turtle.Screen()
        self.win.setup(800,600)
        self.win.bgcolor('black')
        self.win.title('Simple breakout with Python 3 and Turtle with classes')
        self.win.tracer(0)
        self.win.listen()

        self.pen = Scoreboard()
        

    def new_game(self):
        self.x_list = [-340, -230, -120, -10, 100, 210, 320]
        self.y_list = [280, 255, 230, 205, 180]
        self.block_list = []

        self.paddle = Paddle()
        self.ball = Ball(self.paddle, self.block_list)
        self.pen.clear()
        

        for i in self.x_list:
            for j in self.y_list:
                self.block = Block(i,j)
                self.block_list.append(self.block)

        self.run()

    def run(self):
        self.playing = True

        while self.playing:
            self.events()
            self.update()



    def events(self):
        self.win.onkey(self.paddle.move_right, 'Right')
        self.win.onkey(self.paddle.move_left, 'Left')


    def update(self):
        #time.sleep(0.017) # windows?
        
        self.win.update()
        self.ball.move()

        # Block collision check
        for i in self.block_list:
            if i.ycor()-20 <= self.ball.ycor() <= i.ycor()+20 and (i.xcor()-60 < self.ball.xcor()<i.xcor()+60) and self.ball.dy>0:
                i.goto(1000,1000)
                self.ball.dy *= -1
                self.block_list.remove(i)
        # Game over
        if len(self.block_list) < 0 or self.ball.ycor()<-270:
            self.playing = False
            self.ball.goto(1000,1000)
            self.paddle.goto(1000,1000)
            for i in self.block_list:
                i.goto(1000,1000)


    def show_start_screen(self):
        self.waiting = True
        self.pen.goto(0, 0)
        self.win.onkey(self.wait_for_keypress, 'space')
        
        while self.waiting:
            self.win.bgcolor('black')
            self.pen.write('Breakout Game using Python 3 and Turtle\n\n Press the "space" key to continue',
                      align='center', font=('Courier', 24, 'normal'))


    def show_game_over_screen(self):
        self.waiting = True
        self.pen.goto(0, 0)
        self.win.onkey(self.wait_for_keypress, 'space')
        
        while self.waiting:
            self.win.bgcolor('black')
            self.pen.write(f'\t   Game Over \n\n Press the "space" key for new game',
                      align='center', font=('Courier', 24, 'normal'))


    def wait_for_keypress(self):
        self.waiting = False


        





game = Game()
game.show_start_screen()



while True:
    game.new_game()
    game.show_game_over_screen()



