from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(-270,270)
        self.color("black")
        self.level=1
        self.write(f"Level: {self.level}",align="left", font = ("Courier", 15, "normal"))
        
    def level_increment(self):
        self.level+=1
        self.clear()
        self.write(f"Level: {self.level}",align="left", font = ("Courier", 15, "normal"))
    def game_over(self):
        self.goto(-100,-270)
        self.write("GAME OVER",align="left", font = ("Courier", 30, "normal"))