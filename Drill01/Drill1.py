import turtle

def restart():
    turtle.reset()

def moveUp():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def moveDown():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def moveRight():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def moveLeft():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

turtle.shape('turtle')

turtle.onkey(moveUp, 'w')
turtle.onkey(moveDown, 's')
turtle.onkey(moveRight, 'd')
turtle.onkey(moveLeft, 'a')
turtle.onkey(restart, 'Escape')
turtle.listen()
