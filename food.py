#SNAKE'S FOOD
from turtle import Turtle
from random import randint as rd
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.color("white")
        self.refresh_food()

    def refresh_food(self):
        x = rd(-240, 240)
        y = rd(-240, 240)
        self.teleport(x, y)
        self.speed("fast")

