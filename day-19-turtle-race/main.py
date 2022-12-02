from turtle import Turtle, Screen
import random

is_race_on = False
new_turtle = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-80, -60, -40, -20, 0, 20]
all_turtle = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()















# def move_forwards():
#     tim.forward(5)
#
#
# def move_backwards():
#     tim.backward(5)
#
#
# def counter_clockwise():
#     heading = tim.heading()
#     new_heading = heading + 5
#     tim.setheading(new_heading)
#
#
# def clockwise():
#     heading = tim.heading()
#     new_heading = heading - 5
#     tim.setheading(new_heading)
#
#
# def clear_screen():
#     tim.penup()
#     tim.home()
#     tim.clear()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=counter_clockwise)
# screen.onkey(key="d", fun=clockwise)
# screen.onkey(key="c", fun=clear_screen)