#Snake game : hee we will be creating 3 turtles. All games we craete in turtle will ahve different turtle objects. make sure they do not draw anything use penup() for that. for text in turtles also we have to create turtles. in text turtles use write() to give text on screen 
#gegagedigedagedago

#code to move left, right, uop, down with arrow keys or wasd keys.
#xcor() and ycor()  it gets you teh current x and y. Once we get it we will add or subtract a number  from it eG : -0.3 to ycor() do it will make it go down and -0.3 to ycor(0 will amke it go up and voce versa do it with xcor(). When you are changing use set taht means change


#if player goes left, right, up, down wall then it should come backto miff=ddle position, stop snake, shows highscore on screen. 
#if snake crosses left wall that is -350 and right wall that is 350(half width 700). vice versa do for up and down too(take half of 800)

 #if snake touches the fruit, score will +1, fruit will goto random position, size of teh snake will incease. distance function is there which finds the distance between two turtles, if they are close and then they are touching

import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0


# Creating a window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
# the width and height can be put as user's choice
wn.setup(width=600, height=600)
wn.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# food in the game
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 150)
pen.write("Score : 0  High Score : 0", align="center",
          font=("candara", 24, "bold"))


# assigning key directions
def group():
    if head.direction != "down":
        head.direction = "up"


def godown():
    if head.direction != "up":
        head.direction = "down"


def goleft():
    if head.direction != "right":
        head.direction = "left"


def goright():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+30)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-30)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-30)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+30)


wn.listen() 
wn.onkeypress(group, "w") 
wn.onkeypress(godown, "s") 
wn.onkeypress(group, "Up") 
wn.onkeypress(godown, "Down")
wn.onkeypress(goleft, "a") 
wn.onkeypress(goright, "d") 
wn.onkeypress(goleft, "Left") 
wn.onkeypress(goright, "Right")

segments = []


# Main Gameplay
while True:
    wn.update()
    if head.xcor() > 790 or head.xcor() < -790 or head.ycor() > 790 or head.ycor() < -790:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    if head.distance(food) < 20:
        x = random.randint(-300,300)
        y = random.randint(-300, 300)
        food.goto(x, y)

        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    # Checking for head collisions with body segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0: 
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)



#----------------------------------------------Homework-----------------------------------------------
#Create a ping pong game. Create turtles for 5. 2 paddes left and right, 1 for ball. 2 for player1score and player2score.


#----------------------------------------------Homework-----------------------------------------------
#Create a ping pong game. Create turtles for 5. 2 paddes left and right, 1 for ball. 2 for player1score and player2score.

