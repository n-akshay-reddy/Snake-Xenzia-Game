from turtle import Screen
import time
import snake as t
import food as f
import scoreboard



screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = t.Snake()
food = f.Food()
scoreboard = scoreboard.ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
#screen.onkey(scoreboard.reset_score(), "s")







game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) <15:
        food.refresh_food()
        scoreboard.increase_score()
        snake.extend()

    #detect collision with the walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        scoreboard.game_end()
        game_is_on = False

    #detect collision with the tail
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            scoreboard.game_end()
            game_is_on = False








screen.exitonclick()
