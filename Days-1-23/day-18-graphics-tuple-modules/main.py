from turtle import Turtle as t, Screen, colormode
from random import randint
import random


colormode(255)

tim = t()
tim.shape("turtle")
tim.color("green")
# tim.width(10)
tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        tim.circle(70)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(10)



# direction = [tim.fd, tim.bk, tim.rt, tim.lt]
# direction = [0, 90, 180, 270, 360]
#
# def random_walk_go():
#     tim.forward(20)
#     heading = random.choice(direction)
#     tim.setheading(heading)
#     # random.choice(direction)(90)

#
# for _ in range(100):
#     tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
#     random_walk_go()




# sides = 3
# while sides < 10:
#     tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
#     for _ in range(sides):
#         angle = 360 / sides
#         tim.forward(100)
#         tim.right(angle)
#     sides += 1



# for _ in range(20):
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()
#     tim.forward(5)
#
# # for i in range(4):
# #     tim.forward(100)
# #     tim.right(90)







screen = Screen()
screen.exitonclick()