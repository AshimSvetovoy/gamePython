from ColabTurtle.Turtle import *
initializeTurtle()
speed(13)
def drawSquare(size):
  for i in range(0, 4):
    forward(size)
    left(90)

def drawCircle(size):
  for i in range(0, 20):
    forward(size)
    left(360 / 20)

def drawTriangle(size):
  for i in range(0, 3):
    forward(size)
    left(120)

for i in range(0, 20):
  drawSquare(600)
  drawSquare(75)
  drawCircle(100)
  drawTriangle(50)
  forward(360/ 20)
  left(360/20)
