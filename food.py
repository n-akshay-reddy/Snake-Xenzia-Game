import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.turtlesize(stretch_len=0.5, stretch_wid=0.5)
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.refresh_food()

    def refresh_food(self):
        new_x = random.randint(-280,280)
        new_y = random.randint(-280,280)
        self.goto(new_x, new_y)