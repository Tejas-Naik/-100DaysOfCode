import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title('Turtle Racing Game')
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
player.goup()

car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.go_up, 'Up')
screen.onkeypress(player.go_down, 'Down')
screen.onkeypress(player.go_left, 'Left')
screen.onkeypress(player.go_right, 'Right')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 33:
            scoreboard.game_over()
            game_is_on = False

    if player.has_finished():
        player.starting_position()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
