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
    t.up()

    return

def drawGrid(t,size):
    t.down()
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
    return


def setUpTurtle(size):
    # create t, wn
    t = turtle.Turtle()
    wn = turtle.Screen()
    
    # World coordinates: lower left (0,0), upper right (100,100)
    wn.setworldcoordinates(-5, -5, size+5, size+5)
    t.speed(0)
    t.shape("circle")
    t.resizemode("user")
    t.turtlesize(.5,.5)
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
    t.bk(.5)
    t.right(90)
    t.fd(.5)
    t.left(90)

    # fill square
    t.begin_fill()
    for i in range(4):
        t.forward(1)
        t.left(90)
    t.end_fill()

    # redraw lines
    t.down()
    for i in range(4):
        t.forward(1)
        t.left(90)
    t.up()
    
    t.fd(.5)
    t.left(90)
    t.fd(.5)
    t.right(90)
    return



##########
'''MAIN'''
##########

def main():
    size = int(input("What size grid do you want? "))
    t,wn = setUpTurtle(size)
    
    ans = input("Should the grid be drawn? ").lower()
    if ans[0] == "y":
        drawGrid(t,size)

    t.goto(.5,.5)
    t.showturtle()
    print("setup complete")
    
    # movement
    k = input("Move: ").lower()
    while k:
        if k[0] == "q":
            break
        if len(k) > 3 and k[0:2] == "f ":
            fill(t,k[2:])
        
        else:
            for i in range(len(k)):
                if k[i] == "w" or k[i] == "f":
                    up(t)
                elif k[i] == "s" or k[i] == "b":
                    down(t)
                elif k[i] == "d" or k[i] == "r":
                    right(t)
                elif k[i] == "a" or k[i] == "l":
                    left(t)
                elif k[i] == " ":
                    fill(t,"white")
                
        #t.dot()
        k = input("Move: ").lower()

    return

main()
