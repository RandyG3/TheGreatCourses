from turtle import *


def drawtally():
    left(90)
    forward(20)
    backward(20)
    right(90)
    shiftright()


def shiftright():
    penup()
    forward(5)
    pendown()


def drawslash():
    # Move up
    left(90)
    penup()
    forward(3)
    pendown()

    # Draw Slash
    startposition = pos()
    goto(startposition[0]-25, startposition[1]+14)

    # Return to starting position
    penup()
    goto(startposition)
    backward(3)
    right(90)
    pendown()

    # Shift over
    shiftright()
    shiftright()


def drawfive():
    for i in range(5):
        drawtally()
    drawslash()


def drawtallies(n):
    while n >= 5:
        drawfive()
        n = n - 5
    while n >= 1:
        drawtally()
        n = n - 1


num_to_draw = int(input("Enter a number:"))
drawtallies(num_to_draw)

input()