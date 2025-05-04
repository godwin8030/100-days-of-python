from turtle import Turtle, Screen

jack = Turtle()

for steps in range(15):
    jack.forward(10)
    jack.pendown()
    jack.forward(10)
    jack.penup()
