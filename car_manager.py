import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.lst = []
        self.x = 30
        self.move_speed = 0.1

    def create(self):
        t = Turtle()
        t.showturtle()
        t.penup()
        t.shape("square")
        t.color(random.choice(COLORS))
        t.penup()
        t.goto(random.randint(400, 2000) + self.x,random.randint(-270,270))
        for i in range(len(self.lst)):
            while self.lst[i].distance(t) < 150:
                t.goto(random.randint(400, 2000) + self.x, random.randint(-270, 270))

        self.x += 40
        t.shapesize(1,3)
        self.lst.append(t)


    def m(self):
        for i in self.lst:
            i.backward(MOVE_INCREMENT)

    def move_spe(self):
        self.move_speed *= 0.5