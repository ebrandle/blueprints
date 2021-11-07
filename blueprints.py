# Esther Brandle
# Created: 2021/11/06
# Modified: 2021/11/07

import turtle
#import asyncio


###########
'''SETUP'''
###########

def drawLabelBoarders(t,size):
    t.up()
    t.goto(0,-4)
    t.write("(0,0)", align="center",font=11)
    t.goto(0,0)
    t.down()
    t.goto(size,0)
    
    t.up()
    t.goto(size,-4)
    t.write("("+str(size)+",0)", align="center",font=11)
    t.goto(size,0)
    t.down()
    t.goto(size,size)

    t.up()
    t.goto(size-1,size+1)
    t.write("("+str(size)+","+str(size)+")", align="center",font=11)
    t.goto(size,size)
    t.down()
    t.goto(0,size)

    t.up()
    t.goto(0,size+1)
    t.write("(0,"+str(size)+")", align="center",font=11)
    t.goto(0,size)
    t.down()
    t.goto(0,0)

    return

def drawGrid(t,size):
    # draw rows
    for row in range(size // 2):
        t.left(90)
        t.fd(1)
        t.right(90)
        t.fd(size)
        t.left(90)
        t.fd(1)
        t.left(90)
        t.fd(size)
        t.right(180)
    t.up()
    t.goto(0,0)
    t.down()
    
    # draw cols
    for col in range(size // 2):
        t.fd(1)
        t.left(90)
        t.fd(size)
        t.right(90)
        t.fd(1)
        t.right(90)
        t.fd(size)
        t.left(90)

    # return to start
    t.up()
    t.goto(0,0)
    t.down()
    return


def setUpTurtle(size):
    # create t, wn
    t = turtle.Turtle()
    wn = turtle.Screen()
    
    # World coordinates: lower left (0,0), upper right (100,100)
    wn.setworldcoordinates(-5, -5, size+5, size+5)
    #wn.tracer(0)
    t.speed(0)
    t.hideturtle()

    # draw boarders
    drawLabelBoarders(t,size)
    
    return t,wn



###################
'''TURTLE EVENTS'''
###################

def up(t):
    t.left(90)
    t.forward(1)
    t.right(90)

def down(t):
    t.right(90)
    t.forward(1)
    t.left(90)

def right(t):
    t.forward(1)

def left(t):
    t.backward(1)

def fill(t,color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(1)
        t.right(90)
    t.end_fill()



##########
'''MAIN'''
##########

def main():
    size = int(input("What size grid do you want? "))
    t,wn = setUpTurtle(size)
    
    ans = input("Do you want a grid? ").lower()
    if ans == "y" or ans == "yes":
        drawGrid(t,size)
    
    print("setup complete")
    
    # movement
    k = input("Move: ").lower()
    while k != "q":
        if k[0] == "w":
            up(t)
        elif k[0] == "s":
            down(t)
        elif k[0] == "d":
            right(t)
        elif k[0] == "a":
            left(t)
        elif k[0:2] == "f ":
            fill(t,k[2:])
        t.dot()
        k = input("Move: ").lower()

    return

main()
