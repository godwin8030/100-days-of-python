from turtle import Turtle, Screen

jack = Turtle()
screen = Screen()

def move_forwards():
    jack.forward(10)

def move_backwards():
    jack.backward(10)

def turn_left():
    jack.left(10)

def turn_right():
    jack.right(10)

def clear():
    jack.clear()
    jack.penup()
    jack.home()
    jack.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()