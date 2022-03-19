from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.speed("fastest")
        self.write(f"Score : {self.score}", False, "center", ("Courier", 16, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", False, "center", ("Courier", 16, "normal"))

    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "center", ("Courier", 20, "bold"))
