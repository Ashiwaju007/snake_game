from turtle import Turtle
ALIGNMENT = "center"
FONT = ("curial", 24, "normal")




class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        with open("data.txt") as data:
            self.high_score=int(data.read())
        self.score = 0
        self.goto(0, 270)
        self.hideturtle()
        self.count()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def count(self):
        self.score += 1
        self.update_scoreboard()


