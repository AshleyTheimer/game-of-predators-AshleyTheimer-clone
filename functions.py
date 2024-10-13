import copy
import random

def genDataRows(questionNum, state, predators, maxPreds, stock):
    if (questionNum == 1):
        row = [str(maxPreds), str(stock)]
    else:
        if (questionNum == 2):
            headers = ["predLifeLen", "foodEnergy"]
        else: #questionNum = 3
            headers = ["maxPreds", "stock"]
    return row


def perpendicular(predators, predNum):
    direct = 'h'
    if (predators[predNum]['direction'] == 'h'):
        direct = 'v'
    return direct

def gen_repro_option(): # got the idea of the fuction from shakespeare.py
    prob_list = {
        1: .35,
        2: .20,
        3: .15,
        4: .30
    }  # Initialize the prob. dist. dict.
    maxLen = len(prob_list) - 1
    while True:
        randIndex = random.randint(0, maxLen)
        randWord = random.choice(list(prob_list.keys())) # choose random key from dictonary 
        randProb = random.random() # generate probablity 
        if randProb < prob_list[randWord]: # rejection sampling 
            return randWord


def reproduce(side, predators, predNum):
    dead = []
    AD = 2
    predators[predNum]['stockPile'] += -15
    option = gen_repro_option()
    #option = 2 #used to manually test the reproduction options
    print("born option: ", option)
    xcoord = predators[predNum]['x']
    ycoord = predators[predNum]['y']
    newStock = (predators[predNum]['stockPile'])/2
    childNegPos = predators[predNum]['negPos']
    if((option == 1) or (option == 3)):
        predators[predNum]['stockPile'] = newStock
        childNegPos = predators[predNum]['negPos']
        childNegPos = childNegPos*-1
        direct = predators[predNum]['direction']
        if (option == 1):
            direct = perpendicular(predators, predNum)
        predators.append({
            'direction': direct,
            'negPos': childNegPos,
            'stockPile': newStock,
            'x': xcoord,
            'y': ycoord,
            'stepsLived':0
        })
    else:
        i = 1
        direct = predators[predNum]['direction']
        if option == 4:
            newStock = newStock/2
        while i <= option:
            if i == 3:
                direct = perpendicular(predators, predNum)
            childNegPos = (-1) ** i
            #print(direct, childNegPos, "-1 ** ", i)
            predators.append({
                'direction': direct,
                'negPos': childNegPos,
                'stockPile': newStock,
                'x': xcoord,
                'y': ycoord,
                'stepsLived':0
            })
            i += 1
        AD = 1
        dead.append(predNum)
    return predators, dead, AD
    


def updatePredListPos(side, predators, cell):
    #predators[{direction: v, negPos: -1, stockPile: 35, x: 0, y:0}]
    predators[cell]['stepsLived'] += 1
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
            #print("bounce", cell, xcoord) 
        predators[cell]['x'] += predators[cell]['negPos']
    return predators




#Takes argument of 2d array of boolean integers
def updateGoLstate(side, currState, predators, repoStock):
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
       
    
    newState = updatePred(side, newState, predators, repoStock)
    del currState
    return newState
    
def eat(side, newState, predators, cell):
    xcoord = predators[cell]['x']
    ycoord = predators[cell]['y']
    energyGain = 0
    for r in range(5):
        for c in range(5):
            try:
                if (xcoord + c - 2) >= 0 and (ycoord + r - 2) >= 0:
                    if (newState[ycoord + r - 2][xcoord + c - 2] == 1):
                        newState[ycoord + r - 2][xcoord + c - 2] = 0
                        energyGain += 1
            except:
                IndexError
    return newState, energyGain
    


def updatePred(side, newState, predators, repoStock):
    deadPreds = []
    for cell in range(len(predators)):
        
        #print(cell, len(predators), predators[cell]['stockPile']) 
        energyGain = 0
        predators = updatePredListPos(side, predators, cell) #move pos
        predators[cell]['stockPile'] += -5
        xcoord = predators[cell]['x']
        ycoord = predators[cell]['y']
        newstate, energyGain = eat(side, newState, predators, cell)
        predators[cell]['stockPile'] += energyGain
        if (predators[cell]['stockPile'] <= 0):
            AD = 1 # dead, replace with living cell
            deadPreds.append(cell)
            #print("die", cell, predators[cell]['x'], predators[cell]['y'])
        else:
            AD = 2 # lives, keep predator on screen
            #newstate, energyGain = eat(side, newState, predators, cell)
            #predators[cell]['stockPile'] += energyGain
            if (predators[cell]['stockPile'] >= repoStock):
                predators, dead, AD = reproduce(side, predators, cell)
                deadPreds += dead
        for r in range(3):
            for c in range(3):
                newState[ycoord + r - 1][xcoord + c - 1] = AD            
        #print("Gain", energyGain, energyGain-5)
        #predators[cell]['stockPile'] += -5
    i = 0
    deadPreds.sort(reverse=True)
    while i < len(deadPreds):
        index = deadPreds[i]
        #print("cell num die: ", index, "steps lived: ", predators[index]['stepsLived'])
        del predators[index]
        i += 1
    
    return newState