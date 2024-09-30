import copy

def reproduce(side, predators, predNum):
    print("born")
    predators[predNum]['stockPile'] += -15
    newStock = (predators[predNum]['stockPile'])/2
    predators[predNum]['stockPile'] = newStock
    childNegPos = predators[predNum]['negPos']
    childNegPos = childNegPos*-1
    direct = 'h'
    xcoord = predators[predNum]['x']
    ycoord = predators[predNum]['y']
    if (predators[predNum]['direction'] == 'h'):
        direct = 'v'
    predators.append({
        'direction': direct,
        'negPos': childNegPos,
        'stockPile': newStock,
        'x': xcoord,
        'y':ycoord
    })
    return predators
    


def updatePredListPos(side, predators, cell):
    #predators[{direction: v, negPos: -1, stockPile: 35, x: 0, y:0}]
    np = predators[cell]['negPos']
    if (predators[cell]['direction'] == 'v'):
        ycoord = predators[cell]['y']
        if(((ycoord >= side-2)&(np == 1)) or ((ycoord == 1)&(np == -1))):
            predators[cell]['negPos'] = predators[cell]['negPos'] * -1
        predators[cell]['y'] += predators[cell]['negPos']
    else:
        xcoord = predators[cell]['x']
        if(((xcoord >= side-2)&(np == 1)) or ((xcoord == 1)&(np == -1))):
            predators[cell]['negPos'] = predators[cell]['negPos'] * -1
            print("bounce", cell, xcoord) 
        predators[cell]['x'] += predators[cell]['negPos']
    return predators




#Takes argument of 2d array of boolean integers
def updateGoLstate(side, currState, predators):
    newState = copy.deepcopy(currState)
    
    #Calculate neighboring cells for each cell
    
    #Look at each row in state
    for i in range(len(currState)):
        #Look at each column in the row
        for j in range(len(currState[i])):
            #calculate neighbors
            neighbors = 0
            if (currState[i][j] != 2):
                #Add all 9 cells in region centered on current cell
                for k in range(3):
                    for L in range(3):
                        try:
                            if (i + k - 1) >= 0 and (j + L - 1) >= 0:
                                if (currState[i + k - 1][j + L - 1] != 2):
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
            else:
                newState[i][j] = 0
       
    

    del currState
    return newState
    
def updatePred(side, newState, predators):
    deadPreds = []
    for cell in range(len(predators)):
        
        print(cell, len(predators), predators[cell]['stockPile']) 
        xcoord = predators[cell]['x']
        ycoord = predators[cell]['y']
        energyGain = 0
        if (predators[cell]['stockPile'] > 0): # move pred if its alive
            predators = updatePredListPos(side, predators, cell)
            xcoord = predators[cell]['x']
            ycoord = predators[cell]['y']
            for r in range(5):
                for c in range(5):
                    try:
                        if (xcoord + c - 2) >= 0 and (ycoord + r - 2) >= 0:
                            if (newState[ycoord + r - 2][xcoord + c - 2] == 1):
                                newState[ycoord + r - 2][xcoord + c - 2] = 0
                                predators[cell]['stockPile'] += 1 # determine how much this is supposted to increase
                                energyGain += 1
                            if (((r > 0) & (r < 4)) & ((c > 0) & (c < 4))):
                                newState[ycoord + r - 2][xcoord + c - 2] = 2
                    except:
                        IndexError
        else: 
            #print(predators[cell]['amassedEnergy'], predators[cell]['stockPile'])
            deadPreds.append(cell)
            for r in range(3):
                for c in range(3):
                    newState[ycoord + r - 1][xcoord + c - 1] = 1
                    
        print("Gain", energyGain, energyGain-5)
        predators[cell]['stockPile'] += -5
        
        if (predators[cell]['stockPile'] >= 50):
            predators = reproduce(side, predators, cell)
    i = 0
    deadPreds.sort(reverse=True)
    while i < len(deadPreds):
        index = deadPreds[i]
        del predators[index]
        i += 1
    
    return newState