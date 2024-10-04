from turtle import Turtle
UP=90
FIRST_POSTITION=(0,-280)
class TurtleUser(Turtle):
    def __init__(self) :
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(UP)
        self.goto(FIRST_POSTITION)
        
    def move(self):
        self.forward(20)
        
    def reset_position(self):
        self.goto(FIRST_POSTITION)