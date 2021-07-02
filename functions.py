"""
def summation(n1,n2):
    return n1 + n2

summation(2,3)
#print(summation(2,3))
"""
import turtle

def drawSquare(aTurtle, squareSize):
    """Make turtle aTurtle draw a square with side squareSize."""   #docstring accessable at runtime.
    for i in range(4):
        aTurtle.forward(squareSize)
        aTurtle.left(90)

def draw

#Setting up the window and its attributes.
wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()     #Creating a turtle named alex.
drawSquare(alex, 50)       #Alex used as an argument in drawSquare to draw a square of side 50.

#Using alex the turtle to draw another square in a new location
alex.penup()
alex.goto(100,100)
alex.pendown()
drawSquare(alex,75)

wn.exitonclick()