import turtle
import winsound

# window
wn = turtle.Screen()
wn.title("Pong: 1st game project")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
scoreA = 0
scoreB = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)
# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center",
          font=("Courier", 24, "normal"))


# Function
# TODO make a border for the paddle so that it won't go beyond the top and bottom
def upPaddleA():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)


def downPaddleA():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)


def upPaddleB():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)


def downPaddleB():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)


# Keyboard Binding
wn.listen()
wn.onkeypress(upPaddleA, "w")
wn.onkeypress(downPaddleA, "s")
wn.onkeypress(upPaddleB, "Up")
wn.onkeypress(downPaddleB, "Down")

# Main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB),
                  align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB),
                  align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (340 < ball.xcor() < 350) and (paddleB.ycor() + 40 > ball.ycor() > paddleB.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (-340 > ball.xcor() > -350) and (paddleA.ycor() + 40 > ball.ycor() > paddleA.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
