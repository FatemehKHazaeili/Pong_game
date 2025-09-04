from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.rightscore = 0
        self.leftscore = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(0 , 210)
        self.write(f"{self.leftscore} : {self.rightscore}" , align="center", font=("Arial", 24, "bold"))

    def add_score_right(self):
        self.rightscore += 1
        self.clear()
        self.write(f"{self.leftscore} : {self.rightscore}", align="center", font=("Arial", 24, "bold"))

    def add_score_left(self):
        self.leftscore += 1
        self.clear()
        self.write(f"{self.leftscore} : {self.rightscore}", align="center", font=("Arial", 24, "bold"))