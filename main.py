from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.title("Pong")

paddle_right = Paddle(True)
paddle_left = Paddle(False)
ball = Ball()

screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")

while True:
    ball.forward(10)
    ball.check_collision(paddle_right, paddle_left)
    if ball.passed_the_paddle() == "right":
        ball = Ball()
    elif ball.passed_the_paddle() == "left":
        ball = Ball()


screen.exitonclick()