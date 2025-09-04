from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed(1)
        self.speed_range = 1
        self.setheading(45)

    def collision_with_wall(self):
        if self.ycor() > 240 or self.ycor() < -230:
            self.speed(0)
            self.setheading(self.heading() * -1)
            self.speed(self.speed_range)

    def collision_with_paddle(self , paddle):
        if self.xcor() > 360 or self.xcor() < -370:
            if self.distance(paddle) < 30:
                self.speed(0)
                self.speed_range += 0.2
                self.setheading(self.heading() * -1 + 180)
                self.speed(self.speed_range)

    def check_collision(self ,right ,left):
        self.collision_with_paddle(right)
        self.collision_with_paddle(left)
        self.collision_with_wall()

    def passed_the_paddle(self):
        if self.xcor() > 400:
            self.hideturtle()
            return "right"
        elif self.xcor() < -400:
            self.hideturtle()
            return "left"
        return ""

    def start_over(self):
        self.hideturtle()
        self.goto(0, 0)
        self.setheading(self.heading() * -1 + 180)
        self.speed(1)
        self.speed_range = 1
        self.showturtle()