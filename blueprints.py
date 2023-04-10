# Esther Brandle
# Created: 2021/11/06
# Modified: 2023/04/09

import turtle
#import asyncio


###########
'''SETUP'''
###########
def setup():
    # blueprint setup
    fileName = input("Enter a file name to load blueprint (optional): ")
    if fileName != "":
        blueprint,size = loadBlueprint(fileName)
    else:
        size = int(input("What size grid do you want? "))
        blueprint = setUpGrid(size)

    # turtle setup
    t,wn = setUpTurtle(size)
    
    ans = input("Should the grid be drawn? ").lower()
    if ans != "" and ans[0] == "y":
        drawGrid(t,size)

    if fileName != "":
        drawFile(t,blueprint,size)
        t.goto(blueprint[-1][1]+.5,blueprint[-1][0]+.5)
    else:
        t.goto(.5,.5)
        
    t.showturtle()
    print("setup complete")
    return t,blueprint

def drawFile(t,blueprint,size):
    oldEndpoint = blueprint[-1]
    for row in range(size):
        for col in range(size):
            if blueprint[row][col] != '-':
                t.goto(col+.5,row+.5)
                blueprint[-1] = [row,col]
                fill(t,blueprint[row][col],blueprint)
    blueprint[-1] = oldEndpoint

def loadBlueprint(fileName):
    # read from file
    loadFile = open(fileName,"r")
    blueprintLines = loadFile.readlines()
    loadFile.close()

    # initialize blank blueprint
    size = len(blueprintLines)-1
    blueprint = setUpGrid(size)

    # update location
    locationLs = blueprintLines[0].split()
    blueprint[-1][0] = int(locationLs[0])
    blueprint[-1][1] = int(locationLs[1])

    # load blueprint
    for row in range(1,size+1):
        rowLs = blueprintLines[row].split()
        for col in range(size):
            blueprint[size-row][col] = rowLs[col]

    return blueprint,size

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


####################
'''SAVE BLUEPRINT'''
####################
def ask_saveBlueprint(blueprint):
    fileName = input("Enter a file name to save blueprint (optional): ")
    if fileName != "":
        saveBlueprint(fileName,blueprint)

def saveBlueprint(fileName,blueprint):
    saveFile = open(fileName,"w")

    # save location
    saveFile.write(str(blueprint[-1][0])+' '+str(blueprint[-1][1])+'\n')

    # save blueprint
    for row in range(len(blueprint)-2,-1,-1):
        for col in blueprint[row]:
            saveFile.write(col+' ')
        saveFile.write("\n")
    saveFile.close()
    print("Blueprint saved")


##########
'''MAIN'''
##########
def showBlueprint(blueprint):
    print(str(blueprint[-1][0])+", "+str(blueprint[-1][1]))
    for row in range(len(blueprint)-2,-1,-1):
        print(blueprint[row])

def theLoopThatDoesStuff(t,blueprint):
    commandQueue = []
    k = input("Move: ").lower()
    while k:
        # quit
        if k[0] == "q":
            return
        
        # get previous command
        if k in "123456789" and len(k) == 1:
            k = commandQueue[int(k)*(-1)]

        # fill w/ color
        if len(k) > 3 and k[0:2] == "f ":
            fill(t,k[2:],blueprint)

        # move
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
                    
        commandQueue.append(k)
        if len(commandQueue) >= 10:
            commandQueue.pop(0)
        print(commandQueue)
        
        k = input("Move: ").lower()

def main():
    t,blueprint=setup()
    theLoopThatDoesStuff(t,blueprint)
    ask_saveBlueprint(blueprint)
    return

main()
