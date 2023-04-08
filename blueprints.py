# Esther Brandle
# Created: 2021/11/06
# Modified: 2023/04/08

import turtle
#import asyncio


###########
'''SETUP'''
###########

def setUpGrid(size):
    row = ["-"]*size
    grid = []
    for x in range(size):
        grid.append(row[:])
    grid.append([0,0])
    return grid

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

def up(t,blueprint):
    # turtle
    t.left(90)
    t.forward(1)
    t.right(90)

    # logical board
    blueprint[-1][0] += 1
    return blueprint

def down(t,blueprint):
    # turtle
    t.right(90)
    t.forward(1)
    t.left(90)

    # logical board
    blueprint[-1][0] -= 1
    return blueprint

def right(t,blueprint):
    # turtle
    t.forward(1)

    # logical board
    blueprint[-1][1] += 1
    return blueprint

def left(t,blueprint):
    # turtle
    t.backward(1)

    # logical board
    blueprint[-1][1] -= 1
    return blueprint

def fill(t,color,blueprint):
    # turtle
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

    # logical board
    row = blueprint[-1][0]
    col = blueprint[-1][1]
    blueprint[row][col] = color
    return blueprint



##########
'''MAIN'''
##########

def showBlueprint(blueprint):
    print(str(blueprint[-1][0])+", "+str(blueprint[-1][1]))
    for row in range(len(blueprint)-2,-1,-1):
        print(blueprint[row])

def main():
    size = int(input("What size grid do you want? "))
    t,wn = setUpTurtle(size)
    blueprint = setUpGrid(size)
    
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
            fill(t,k[2:],blueprint)
        
        else:
            for i in range(len(k)):
                if k[i] == "w" or k[i] == "f":
                    up(t,blueprint)
                elif k[i] == "s" or k[i] == "b":
                    down(t,blueprint)
                elif k[i] == "d" or k[i] == "r":
                    right(t,blueprint)
                elif k[i] == "a" or k[i] == "l":
                    left(t,blueprint)
                elif k[i] == " ":
                    fill(t,"white",blueprint)
        showBlueprint(blueprint)
                    
        #maybe add action queue w/ ^?
                    
        #t.dot()
        k = input("Move: ").lower()

    return

main()
