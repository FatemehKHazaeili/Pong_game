from turtle import Turtle

class Paddle(Turtle):
    def __init__(self , right):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=3, stretch_len=0.2)
        self.set_paddle_pos(right)
        self.color("white")

    def set_paddle_pos(self , right):
        if right:
            self.setposition(370 , 0)
        else:
            self.setposition(-380 , 0)

    def move_up(self):
        if self.ycor() < 210:
            self.sety(self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -210:
            self.sety(self.ycor() - 20)