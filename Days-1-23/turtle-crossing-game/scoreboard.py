from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1
        self.scoreboard()

    def scoreboard(self):
        self.goto(-250, 260)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 260)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def new_point(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

