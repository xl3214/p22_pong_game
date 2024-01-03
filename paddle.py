from turtle import Turtle

STARTING_POSITION = (350, 0)
WALLS = (380, 270)
SIDES = {'left': -1, 'right': 1}
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.create_paddle(side)

    def create_paddle(self, side):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed('fastest')
        self.penup()
        new_position = (STARTING_POSITION[0] * SIDES[side], STARTING_POSITION[1])
        self.goto(new_position)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        if new_y < WALLS[1]:
            self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        if new_y > WALLS[1] * -1:
            self.goto(self.xcor(), new_y)
