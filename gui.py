import turtle

turtle.setup(400, 300)
turtle.bgcolor("black")

paddle1 = turtle.Turtle()
paddle1.shape("square")
paddle1.color("black")
paddle1.shapesize(stretch_wid=1, stretch_len=5)
paddle1.penup()
paddle1.goto(-350, 0)
paddle1.dy =0

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.goto(0,0)

game_over = False
winner = None
points = {
    "player 1": 0
}
game_rules = {
    "max_points": 3,
    "ball_speed": 4
}