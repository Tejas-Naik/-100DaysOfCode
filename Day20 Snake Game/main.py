from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Windows Snake Game')
# the tracer function will not show the animation
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

game_is_on = True

while game_is_on:
    screen.update()  # the update function shows the animation
    time.sleep(0.1)  # making the snake's tail to head of snake
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    wall_collision = [
        snake.head.xcor() > 290,
        snake.head.xcor() < -290,
        snake.head.ycor() > 290,
        snake.head.ycor() < -290,
    ]
    if any(wall_collision):
        # game_is_on = False
        scoreboard.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
