import turtle
import random


segment = []
ground = turtle.Screen()
snake = turtle.Turtle()
food = turtle.Turtle()
scoreboard = turtle.Turtle()


ground.addshape("head up.gif")
ground.addshape("head down.gif")
ground.addshape("head left.gif")
ground.addshape("head right.gif")
ground.addshape("body.gif")

snake.shape("head up.gif")
food.shape("circle")
food.color("red")
ground.bgpic("grass.gif")


scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(250,250)
snake.penup()
food.penup()
food.goto(100,0)

#score
scoreboard.write("score - 0 -",font=("Arial",15,"bold"))

#move
def up():
   if snake.heading() != 270:
    snake.shape("head up.gif")
    snake.setheading(90)
    snake.forward(20)
def down():
    if snake.heading() != 90:
        snake.shape("head down.gif")
        snake.setheading(270)
        snake.forward(20)
def left():
    if snake.heading() != 0:
        snake.shape("head left.gif")
        snake.setheading(180)
        snake.forward(20)
def right():
    if snake.heading() != 180:
        snake.shape("head right.gif")
        snake.setheading(0)
        snake.forward(20)
#calling
turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")
turtle.listen()
#food
score = 0
while True:
    ground.update()
    x = random.randint(-260,260)
    y = random.randint(-260,260)

    # for i in segment[5:]:
    #     if i.distance(snake)<10:
    #         ground.bgpic("game over.gif")
    #         food.hideturtle()
    if food.distance(snake) < 20:
        food.clear
        score+=1
        scoreboard.clear()
        scoreboard.write(f"score - {score} -",font=("Arial",15,"bold"))
        food.speed(1000)
        food.goto(x,y)
        body = turtle.Turtle()
        body.shape("body.gif")
        body.speed(0)
        body.penup()
        segment.append(body)

    for i in range (len(segment)-1,0,-1):
        x = segment[i-1].xcor()
        y = segment[i-1].ycor()
        segment[i].goto(x,y)

    if len(segment)>0:
        x = snake.xcor()
        y = snake.ycor()
        segment[0].goto(x,y)

    if snake.xcor()>270 or snake.xcor()<-270 or snake.ycor()>270 or snake.ycor()<-270:
        ground.bgpic("game over.gif")
        food.hideturtle()


        

turtle.done()
