from turtle import  Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.title("Snake Game")
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.right,"Right")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
game_is_on = True

while game_is_on :
    screen.update()
    time.sleep(0.1)
    snake.move()
    score.display_score()

    if snake.head.distance(food) < 15 :
        food.refresh()
        score.current_score += 1
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 300 or snake.head.ycor() < -280 :
        game_is_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10 :
            game_is_on = False
            score.game_over()

screen.exitonclick()
