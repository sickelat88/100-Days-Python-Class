from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.my_score = 0
        self.color("white")
        self.goto(0, 260)
        self.clear()
        self.hideturtle()
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.my_score}   High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def new_point(self):
        self.my_score += 1
        self.update_scoreboard()

    def reset(self):
        if self.my_score > self.high_score:
            self.high_score = self.my_score
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
        self.my_score = 0
        self.update_scoreboard()


