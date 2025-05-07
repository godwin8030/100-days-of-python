from turtle import Turtle

STARTING_POS = [(0,0), (-20,0), (-40,0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for positon in STARTING_POS:
            self.add_seg(positon)
            

    def add_seg(self, position):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def extend(self):
        self.add_seg(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DIST)


    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)