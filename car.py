from turtle import Turtle
from random import randint

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.car_speed=0.1
        self.random_position()
        
        self.random_color()
        
    def random_position(self)  :
        self.random_x=randint(-280,2000)
        self.random_y=randint(-240,240)
        self.goto(self.random_x,self.random_y)
        
    def random_color(self):
        color_r=randint(0,255)
        color_g=randint(0,255)
        color_b=randint(0,255)
        self.color(color_r,color_g,color_b)
        
        
    def car_move(self):
        new_x=self.xcor()-10
        self.goto(new_x,self.ycor())
        self.reset_cars()
        
    def new_level(self):
        self.car_speed*=0.9
        self.random_position()
        
    def reset_cars(self):
        if self.xcor()<-400:
            self.random_x=randint(300,2000)
            self.random_y=randint(-240,240)
            self.goto(self.random_x,self.random_y)
        
    
    
        