from turtle import Screen
from score import ScoreBoard
from ball import Ball
from paddle import Paddle
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Kristal's First Pong Game")
player_num = screen.numinput("Players", "How many players? Type 1 or 2: ", minval=1, maxval=2)
difficulty = screen.textinput("Difficulty", "Which level of difficulty would you like? "
                                            "Type 'easy', 'medium', or 'hard'.")
screen.listen()

p1 = Paddle(side="left")
p2 = Paddle(side="right")
ball = Ball()
score_board = object
score_board1 = object
score_board2 = object
if player_num == 1:
    score_board = ScoreBoard()
elif player_num == 2:
    score_board1 = ScoreBoard(position=(-200, 270))
    score_board2 = ScoreBoard(position=(200, 270))

KEYS = {"Up": p2.move_up, "Down": p2.move_down, "w": p1.move_up, "s": p1.move_down}

for key in KEYS:
    screen.onkey(key=key, fun=KEYS[key])

game_on = True
while game_on:
    screen.update()
    if difficulty == "easy":
        time.sleep(0.1)
    elif difficulty == "medium":
        time.sleep(0.05)
    else:
        time.sleep(0.01)

    ball.move()

    if player_num == 1:
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        if ball.distance(p1) < 50 and ball.xcor() < -320 or ball.distance(p2) < 50 and ball.xcor() > 320:
            ball.bounce_x()
            score_board.increase_score()
        if ball.xcor() < -400 or ball.xcor() > 400:
            game_on = False
            score_board.game_over()

    elif player_num == 2:
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        if ball.distance(p2) < 50 and ball.xcor() > 320:
            ball.bounce_x()
            score_board2.increase_score()
        if ball.distance(p1) < 50 and ball.xcor() < -320:
            ball.bounce_x()
            score_board1.increase_score()
        if ball.xcor() < -400:
            ball.reset_position()
            score_board2.increase_score()
        if ball.xcor() > 400:
            ball.reset_position()
            score_board1.increase_score()


screen.exitonclick()
