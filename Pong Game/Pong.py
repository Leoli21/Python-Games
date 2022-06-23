import turtle
import winsound

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(2)

# Score
p1Score = 0
p2Score = 0


# Paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square") #default dimensions of square is 20x20
paddle1.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)

# Paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")   #default dimensions of square is 20x20
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.color("white")
paddle2.penup()
paddle2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(6)
ball.shape("square")   #default dimensions of square is 20x20
ball.color("white")
ball.penup()
ball.goto(0, 0)
# Ball Movement
ball.dx = 1
ball.dy = -1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def paddle1Up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

def paddle1Down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)

def paddle2Up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)

def paddle2Down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)


#Keyboard binding
window.listen()
window.onkeypress(paddle1Up, "w")
window.onkeypress(paddle1Down, "s")
window.onkeypress(paddle2Up, "Up")
window.onkeypress(paddle2Down, "Down")


# Main Game Loop

while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Collision
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
        p1Score += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(p1Score, p2Score), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        p2Score += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(p1Score, p2Score), align="center", font=("Courier", 24, "normal"))


    # Paddle and Ball Collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


