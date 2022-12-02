from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen. bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# call paddle
player_paddle = Paddle((350, 0))
comp_paddle = Paddle((-350, 0))

# call ball
ball = Ball()

# call scoreboard
scoreboard = Scoreboard()

# listen for keys to move player paddle
screen.listen()
screen.onkey(player_paddle.up, "Up")
screen.onkey(player_paddle.down, "Down")
screen.onkey(comp_paddle.up, "w")
screen.onkey(comp_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # bounce
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(player_paddle) < 50 and ball.xcor() > 320 or ball.distance(comp_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # if comp point is scored
    if ball.xcor() > 370:
        ball.ball_reset()
        scoreboard.l_point()

    # if player point is scored
    if ball.xcor() < -370:
        ball.ball_reset()
        scoreboard.r_point()


screen.exitonclick()
