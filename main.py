import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
p = Player()
c = CarManager()
sco = Scoreboard()
screen.title("Turtle cross road")
screen.listen()
game_is_on = True
while game_is_on:
    if p.ycor() > 280:
        c.move_spe()
        p.r()
        sco.level_up()

    for i in c.lst:
        if p.distance(i) < 30:
            sco.game_over()
            game_is_on = False

    c.create()
    time.sleep(c.move_speed)
    screen.update()
    screen.onkey(p.move, "Up")
    c.m()

screen.exitonclick()