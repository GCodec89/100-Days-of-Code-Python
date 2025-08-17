from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

INITIAL_SNAKE = 3
SPEED = 0.1
MIN_SPEED = 0.04

my_screen = Screen()
my_screen.setup(height=600, width=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

snake = Snake(INITIAL_SNAKE)
food = Food()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(snake.snake_up, "Up")
my_screen.onkey(snake.snake_down, "Down")
my_screen.onkey(snake.snake_right, "Right")
my_screen.onkey(snake.snake_left, "Left")

game_is_on = True

while game_is_on:
    my_screen.update()
    time.sleep(SPEED)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.refresh_scoreboard()
        SPEED = max(SPEED * 0.98, MIN_SPEED)

    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        game_is_on = False
        scoreboard.game_over()
    
    for body in snake.body[1:]:
        if snake.head.distance(body) < 10:
            game_is_on = False
            scoreboard.game_over()

my_screen.exitonclick()
