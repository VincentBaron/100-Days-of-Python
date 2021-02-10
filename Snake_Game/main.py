import time
from turtle import Screen
from snake import Snake
from food import *
from score import *

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake.py")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
snake.create_snake()
movement = 1
while movement:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.blocks[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update()
    if snake.blocks[0].xcor() > 280 or snake.blocks[0].xcor() < -280 or snake.blocks[0].ycor() > 280 or snake.blocks[0].ycor() < -280:
        movement = False
        score.game_over()
    for block in snake.blocks[1:]:
        if snake.blocks[0].distance(block) < 15:
            movement = False
            score.game_over()


screen.exitonclick()