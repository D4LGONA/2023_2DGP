import turtle
from random import *
from math import *

def restart():
    turtle.reset()

ptx = randint(-300,300) - 40
pty = randint(-300,300) - 40
score = 0

def turtleInCircle():
    global ptx, pty, score
    if(turtle.distance(ptx, pty) < 40):
        turtle.reset()
        ptx = randint(-300,300) - 40
        pty = randint(-300,300) - 40
        makeCircle(ptx, pty)
        score+=1
        print(score)

def moveUp():
    turtle.setheading(90)
    turtle.forward(20)
    turtle.stamp()
    turtleInCircle()
    
def moveDown():
    turtle.setheading(270)
    turtle.forward(20)
    turtle.stamp()
    turtleInCircle()

def moveRight():
    turtle.setheading(0)
    turtle.forward(20)
    turtle.stamp()
    turtleInCircle()

def moveLeft():
    turtle.setheading(180)
    turtle.forward(20)
    turtle.stamp()
    turtleInCircle()

def makeCircle(x,y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(40)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()


turtle.shape('turtle')

makeCircle(ptx, pty)

turtle.onkey(moveUp, 'w')
turtle.onkey(moveDown, 's')
turtle.onkey(moveRight, 'd')
turtle.onkey(moveLeft, 'a')
turtle.onkey(restart, 'Escape')
turtle.listen()








