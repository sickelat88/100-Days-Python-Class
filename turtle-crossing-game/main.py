
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# call turtle
turtle = Player()

# call cars
car_manager = CarManager()

# call scoreboard
scoreboard = Scoreboard()

# listen for keys to move turtle up
screen.listen()
screen.onkey(turtle.move_turtle, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            scoreboard.game_over()
            game_is_on = False

    # detect successful crossing
    if turtle.ycor() > 280:
        turtle.new_turtle()
        car_manager.increase_speed()
        scoreboard.new_point()

screen.exitonclick()




