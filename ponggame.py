import turtle


#create screen
screen=turtle.Screen()
screen.title("Snake Game")
screen.setup(width=700, height=800)
screen.bgcolor("white")

player2=turtle.Turtle()
player2.shape("square")
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.color("black")
player2.penup()
player2.goto(600,0)

ball=turtle.Turtle()
ball.shape("circle")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.color("black")
ball.penup()
ball.goto(0,0)

score1=turtle.Turtle()
score1.color("black")
score1.penup()
score1.goto(-300,300)
score1.hideturtle()
score1.write("Score 1:   ", align="center", font=("Verdana", 30, "bold"))

score2=turtle.Turtle()
score2.color("black")
score2.penup()
score2.goto(300,300)
score2.hideturtle()
score2.write("Score 2:     ", align="center", font=("Verdana", 30, "bold"))
player1score=0
player2score=0

player1=turtle.Turtle()
player1.shape("square")
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.color("black")
player1.penup()
player1.goto(-600,0)
def up():
 y=player1.ycor()
 y=y+20 
 player1.sety(y)
def down():
 y=player1.ycor()
 y=y-20 
 player1.sety(y)
screen.listen()
screen.onkeypress(up,"w")
screen.onkeypress(down,"s")
#dx and dy is just teh variable to give speed to the ball.
ball.dx=9
ball.dy=-9
#while loop is imprtant for game to go on. In turtle there is no bounce property s we can give if then that say ifour bakk tries cris=ossing certaing valuemon left, right, upm don side the it comes back
while True:
  screen.update()
  #in below line we change x and y using stex and sety. to change we add speed to te ccurrent position. xcor() is current position and x is teh speed
  ball.setx(ball.xcor()+ball.dx)
  ball.sety(ball.ycor()+ball.dy)
  #mark second player move by following the ball x and y
  player2.sety(ball.ycor())
  
  #in the above code we are moving the ball by adding some speed to the current(xcor)
  #bounceing teh ball by giving if that if ball crosses left side then it becones back to middle or some other position and may be change teh speed, also increase the score and rewrite score again
  #take always of the size : 700 its 350
  #For it wil be less than -350 and for right it will greater tahn 350
  if ball.xcor()<-700:
    ball.goto(0, 0)
    ball.dx*=-1
    player2score+=1
    score2.clear()
    score2.write("Score 2: {}  ".format(player2score), align="center", font=("Verdana", 30, "bold"))
  if ball.xcor()>700:
    ball.goto(0, 0)
    ball.dx*=-1
    player1score+=1
    score1.clear()
    score1.write("Score 1: {}  ".format(player1score), align="center", font=("Verdana", 30, "bold"))
  if ball.ycor()<-500:
    ball.sety(-400)
    ball.dy*=-1
  if ball.ycor()>500:
    ball.sety(400)
    ball.dy*=-1
  if ball.distance(player1)<40 and ball.xcor()<-500:
    ball.setx(-500)
    ball.dx*=-1
    ball.dy*=-1
  if ball.distance(player2)<40 and ball.xcor()>500:
    ball.setx(500)
    ball.dx*=-1
    ball.dy*=-1