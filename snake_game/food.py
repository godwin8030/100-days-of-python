from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_xpos = random.randint(-280, 280)
        random_ypos = random.randint(-280, 280)
        self.goto(random_xpos, random_ypos)
    