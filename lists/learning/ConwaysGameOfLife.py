# Conway's Game of Life

# cellular Automata
'''
set of rules governing the behavior of a field made up of discrete 
cells. A filled-in square will be “alive” and an empty square will be
 “dead.” If a living square has two or three living neighbors,
 t continues to live on the next step. If a dead square has exactly 
 three living neighbors, it comes alive on the next step. 
Every other square dies or remains dead on the next step.

'''
## list of lists to represent the 2d field

##inner list = collumn of squares #  for living and ' ' for dead

import random, time, copy

WIDTH = 60
HEIGHT = 20

# list of lists for the cells
                    #   y1,y2,y3,y4,y5,y6
nextCells = [] # e.g. [[#,#,' ',' ', ' ',#],[' ', ' ', ' ', #, # , #], ..., [#,' ',' ', #, ' ',#]] 
                    #         x1                    x2                              x3
for x in range(WIDTH):
    column = [] # create column, repeats WIDTH times and adds each to
                # next cells list
    
    for y in range(HEIGHT): # add living cells (50:50 chance of a cell
                            # being living or dead)
        if random.randint(0,1) == 0:
            column.append('#') # add living cell
        else:
            column.append(' ') # add a dead cell
    nextCells.append(column) # add the column to nextCells
        # nextCells is a list of column lists
    
## first step of automata is random ##

# list of lists structure to store # or ' ' stings for cells,
# place on list of lists represents place on screen

# first step in main program will be to copy nextCells to currentCells
# for List of lists data structure x-coord start at 0 on left and inc-
# -rease going right, y-coord start at 0 on top, increase down
# so nextCells[0][0] is top left, nextCells[x][y]
# nextCells[1][0] to the right of top left and nextCells[0][1] below
# the top left cell.

while True: # main program loop
    print('\n\n\n\n\n') # separate each step with new lines
    currentCells = copy.deepcopy(nextCells)
    
## print current cells on screen ##

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # prints '#' or space ' '
            # no new-line with each iteration of x,y.
        print() # prints new line at end of row

# nested for loops ensure printing a full row of cells and then 
# newline character at the end of the row. Repeat for each row
# in nextCells

    # calculate the next step's cells based on current steps cells

    for x in range(WIDTH):
        for y in range(HEIGHT):
            # get neighbouring coords
            # '% WIDTH' ensures left coord is always between 0
            # and WIDTH-1

            leftCoord  = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

# next we need to use two nested for loops to calculate each cell
# for the next step. The living or dead state of the cell depends
# on the neighbour calculate the index of the cells to left, right,
# above and below the current x y coords.

# % mod operator performs a 'wraparound' The left neighbor of a cell in 
# the leftmost column 0 would be 0 - 1 or -1. To wrap this around to the
# rightmost columns index, 59, we calculate (0 - 1) % WIDTH. 
# Since WIDTH is 60, this expression evaluates to 59. This 
# mod-wraparound technique works for the right, above, 
# and below neighbors as well.

# count number of living neighbouring cells #

# do not use elif here as these statements are not mutally exclusive, 
# they could all happen at once

            numNeighbours = 0
            # going round clockwise
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbours += 1 # top left neighbour alive

            if currentCells[x][aboveCoord] == '#':
                numNeighbours += 1 # top neighbour alive

            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbours += 1 # top right neighbour alive

            if currentCells[rightCoord][y] == '#':
                numNeighbours += 1 # left neighbour alive

            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbours += 1 # bottom right neighbour alive

            if currentCells[x][belowCoord] == '#':
                numNeighbours += 1 # bottom neighbour alive

            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbours += 1 # bottom left neighbour alive

            if currentCells[leftCoord][y] == '#':
                numNeighbours += 1 # left neighbour alive
            
            # decide if the cell at nextCells[x][y] is living or dead
            # look at the number of living neighbours currentCells[x][y]
            # has.

            # Set cells based on Conway's game of lift rules:
            # (note still in the for loop iterating over x and y)

            # note these next statements are not mutally exclusive
            # only one can occur
            if currentCells[x][y] == '#' and (numNeighbours == 2 or numNeighbours == 3):
                nextCells[x][y] = '#'
                # living cells with 2 or 3 neighbours remain alive
            elif currentCells[x][y] == ' ' and numNeighbours == 3:
                nextCells[x][y] = '#'
                # dead cells with 3 neighbours become alive
            else:
                nextCells[x][y] = ' '
                # everything else dies or remains dead
    time.sleep(1) # 1 second pause reduces flickering

            # program execution then goes back to the start of
            # the main program loop to continue to next step
        

            
            
            