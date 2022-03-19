from turtle import Screen
from Snake import Snake
import time
import food
from scoreboard import ScoreBoard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)
my_screen.listen()

score_Board = ScoreBoard()
snake = Snake()
snacks = food.Food()

game_is_on = True

my_screen.onkey(key="Up", fun=snake.up)
my_screen.onkey(key="Down", fun=snake.down)
my_screen.onkey(key="Right", fun=snake.right)
my_screen.onkey(key="Left", fun=snake.left)

while game_is_on:
    my_screen.update()
    time.sleep(0.05)
    snake.move()
    if snake.segments[0].distance(snacks) < 15:
        snake.grow()
        snacks.update()
        score_Board.update_score()
    if (abs(snake.segments[0].xcor()) > 280) or (abs(snake.segments[0].ycor()) > 280):
        game_is_on = False
        score_Board.gameover()
    headless = snake.segments[1:]
    for segment in headless:
        if snake.segments[0].distance(segment) < 15:
            game_is_on = False
            score_Board.gameover()
print("You lost !")
my_screen.exitonclick()
