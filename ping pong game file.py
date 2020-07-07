import turtle
import winsound
wn = turtle.Screen()
wn.title('Pong')
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
ball_dx = 0.5
ball_dy = 0.5
# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
#score
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player A:0 player B:0", align="center", font=("Areial", 22, "normal"))

global score_a
global score_b
score_a=0
score_b=0

def paddle_a_up():
    y = paddle_a.ycor()

    if paddle_a.ycor() + 70 > 300:
        paddle_a.sety(y)
    else:
        y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if paddle_a.ycor() - 70 < -300:
        paddle_a.sety(y)
    else:
        y -= 20
        paddle_a.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if paddle_b.ycor() - 70 < -300:
        paddle_b.sety(y)
    else:
        y -= 20
        paddle_b.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if paddle_b.ycor() + 70 > 300:
        paddle_b.sety(y)
    else:
        y += 20
        paddle_b.sety(y)


def score(a,b):
    pen.clear()
    pen.write("player A:{} player B:{}".format(a,b), align="center", font=("Areial", 22, "normal"))


# main game
while True:
    
    wn.listen()
    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")
    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")

    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)
    if ball.ycor() > 290:
        ball.sety(290)
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        ball_dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball_dy *= -1
    if ball.xcor() > 380:
        ball.goto(0, 0)
        score_a+=1
        score(score_a,score_b)
        ball_dx *= -1
    elif ball.xcor() < -380:
        ball.goto(0, 0)
        score_b+=1
        score(score_a, score_b)
        ball_dx *= - 1
    if ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball_dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.setx(340)
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball_dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.setx(-340)

    wn.update()
