from turtle import forward, backward, left, right, penup, pendown


def drawtriangle(size=100):
    for i in range(3):
        forward(size)
        left(120)


def drawsquare(size=100):
    for i in range(4):
        forward(size)
        left(90)


def drawhouse(size=100):
    # Draw Base
    drawsquare()

    # Repos Turtle
    left(90)
    forward(size)
    right(90)

    # Draw top
    drawtriangle()

    # move back to start
    right(90)
    forward(size)
    left(90)


drawhouse()