# snake class in OOP
from turtle import Screen, Turtle

ALL_TURTLES = []
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.ALL_TURTLES = []
        self.x = 0
        self.create_snake()
        self.head = self.ALL_TURTLES[0]

    def create_snake(self):
        for position in range(1, 4):
            self.add_segment(position)


    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        self.x -= 20
        new_turtle.goto(x=self.x, y=0)
        self.ALL_TURTLES.append(new_turtle)

    def reset(self):
        for seg in self.ALL_TURTLES:
            seg.goto(1000, 1000)
        self.ALL_TURTLES.clear()
        self.create_snake()
        self.head = self.ALL_TURTLES[0]

    def extend(self):
        self.add_segment(self.ALL_TURTLES[-1].position())


    def move(self):
        for seg_num in range(len(self.ALL_TURTLES) - 1, 0, -1):
            new_x = self.ALL_TURTLES[seg_num - 1].xcor()
            new_y = self.ALL_TURTLES[seg_num - 1].ycor()
            self.ALL_TURTLES[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)