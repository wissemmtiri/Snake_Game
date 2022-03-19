from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed("fastest")
        y = random.randint(-280, 280)
        x = random.randint(-280, 280)
        self.goto(x, y)

    def update(self):
        y = random.randint(-280, 280)
        x = random.randint(-280, 280)
        self.goto(x, y)
