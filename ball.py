from turtle import Turtle
from random import randint
MOVE_DISTANCE = 20

STARTING_POSITION = (0, 0)
DIRECTIONS = {"down_right": (270, 360), "up_left": (90, 180), "up_right": (0, 90), "down_left": (180, 270), }


class Ball(Turtle):
    def __init__(self):
        """Create the ball and make it move"""
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """Move; Detect collision with wall and bounce"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Bounce between up/down walls"""
        self.y_move *= -1

    def bounce_x(self):
        """Bounce between paddles"""
        self.x_move *= -1
        # The code below did not work because self.goto can change the ball's direction.
        # current_position = self.pos()
        # current_heading = self.heading()
        # if current_heading < 90:  # Heading right up
        #     self.setheading(randint(90, 180))
        #     self.goto(current_position[0] - 10, current_position[1] - 10)
        # elif current_heading >= 270:  # Heading right down
        #     self.setheading(randint(180, 269))
        #     self.goto(current_position[0] - 10, current_position[1] + 10)
        # elif current_heading < 180:  # Heading left up
        #     self.setheading(randint(0, 89))
        #     self.goto(current_position[0] + 10, current_position[1] - 10)
        # elif current_heading < 270:  # Heading left down
        #     self.setheading(randint(270, 359))
        #     self.goto(current_position[0] + 10, current_position[1] + 10)

    def reset_position(self):
        """Reset the ball to center once misses, and move in opposite direction"""
        self.goto(0, 0)
        self.bounce_x()
        # current_heading = self.heading()
        # new_heading = (current_heading + 180) % 360
        # self.setheading(new_heading)
