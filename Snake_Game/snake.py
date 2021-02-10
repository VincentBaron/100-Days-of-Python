from turtle import *

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.blocks = []

    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_block(i)


    def add_block(self, i):
        block = Turtle("square")
        block.color("white")
        block.penup()
        block.goto(i)
        self.blocks.append(block)

    def extend(self):
        self.add_block(self.blocks[-1].position())


    def move(self):
        for block in range(len(self.blocks) - 1, 0, -1):
            self.blocks[block].goto(self.blocks[block - 1].xcor(), self.blocks[block - 1].ycor())
        self.blocks[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.blocks[0].heading() != 270:
            self.blocks[0].setheading(90)

    def down(self):
        if self.blocks[0].heading() != 90:
            self.blocks[0].setheading(270)

    def left(self):
        if self.blocks[0].heading() != 0:
            self.blocks[0].setheading(180)

    def right(self):
        if self.blocks[0].heading() != 180:
            self.blocks[0].setheading(0)
