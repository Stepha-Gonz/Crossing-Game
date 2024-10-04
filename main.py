import turtle as t
import time
from turtle_user import TurtleUser
from scoreboard import Scoreboard
from car import Car


screen=t.Screen()
screen.title("Crossing Game-StephaGonz")
screen.setup(600,600)
screen.colormode(255)
screen.tracer(0)

#color


turtle_user=TurtleUser()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(turtle_user.move,"Up")
car_list=[]
for i in range(50):
    cars=Car()
    car_list.append(cars)
    

is_game_one=True

while is_game_one:
    
    screen.update()
    time.sleep(cars.car_speed)
    for i in car_list:
        i.car_move()

    if turtle_user.ycor()>280:
        scoreboard.level_increment()
        turtle_user.reset_position()
        for i in car_list:
            i.new_level()
    for i in car_list:
        if turtle_user.distance(i)<25:
            scoreboard.game_over()
            screen.update()
            is_game_one=False
        














screen.exitonclick()