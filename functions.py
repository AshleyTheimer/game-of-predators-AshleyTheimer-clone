import copy

#Takes argument of 2d array of boolean integers
def updateGoLstate(currState):
    newState = copy.deepcopy(currState)
    
    #Calculate neighboring cells for each cell
    
    #Look at each row in state
    for i in range(len(currState)):
        #Look at each column in the row
        for j in range(len(currState[i])):
            #calculate neighbors
            neighbors = 0
            
            #Add all 9 cells in region centered on current cell
            for k in range(3):
                for L in range(3):
                    try:
                        if (i + k - 1) >= 0 and (j + L - 1) >= 0:
                            neighbors += currState[i + k - 1][j + L - 1]
                    except:
                        IndexError
            
            neighbors += -1*currState[i][j] #Subtract the self
            
            #print(i, j, neighbors)
                        
            #Rule 1:
            #    If dead, born if exactly 2 neighbors
            if currState[i][j] == 0 and neighbors == 2:
                newState[i][j] = 1
            #Rule 2:
            #    If alive, and 2-3 neighbors, stay alive -- needs no updates
            #Rule 3:
            #    If alive, and <2 or >3 neighbors, die
            if currState[i][j] == 1 and not (neighbors == 2 or neighbors == 3):
                newState[i][j] = 0
            

    del currState
    return newState