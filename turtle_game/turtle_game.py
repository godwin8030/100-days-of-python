from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Please make your bet", prompt="Which turtle will win ? Enter a color: ")
colors = ["red", "purple", "violet", "yellow", "green", "blue "]
y_positions = [-70, -40, -10, 20, 50, 80]
x_positions = [50, 70, 90, 110, 130, 150]
all_turtles =  []

for turtle_num in range(0,5):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_num])
        new_turtle.penup()
        new_turtle.goto(x=-190, y=y_positions[turtle_num])
        all_turtles.append(new_turtle)

if user_bet:
        race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
              race_on = False
              winning_color = turtle.pencolor()
              if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!!")
              else:
                print(f"You have lost! The {winning_color} turtle is the winner!!")

        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)


screen.exitonclick()