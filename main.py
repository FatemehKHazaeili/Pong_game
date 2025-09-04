from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.title("Pong")

paddle_right = Paddle(True)
paddle_left = Paddle(False)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")

while True:
    ball.forward(10)
    ball.check_collision(paddle_right, paddle_left)
    if ball.passed_the_paddle() == "right":
        ball.start_over()
        scoreboard.add_score_left()
    elif ball.passed_the_paddle() == "left":
        ball.start_over()
        scoreboard.add_score_right()


screen.exitonclick()