#Conway's Game Of Life
#Author: RR & CIS343-F24
#Last Updated: 9/24/2024
#python gameOfLife.py

#Goals: Simulate Conway's GoL
#       Simulate a random initial state of the system
#       Visualize the state of the system in each step
#       Analyze how many cells are alive per step

import random
import matplotlib.pyplot as plt
import functions as gol

seeVisuals = 0 # 0 for off 1 for on


# Pick the question you want to collect data about
#   1. How does the maximum number of predators suported by a system depend on how much stockpile is needed to reproduce in the predator lifecycle?
#   2. How does the length of a predator's life depend on the efficiency of its energy consumption (e.g., how many units of 'food' it gains per cell it 'eats')?
#   3. If the base rules of the Game of Life are changed, such that the cells have evolved to survive under conditions with 4 surrounding neighbors (but perish 
#      with 5 neighbors), does this increase or decrease the maximum number of predators which can be sustained in the system?

questionNum = 2 #user change number here

if (questionNum == 1):
    file_name = "GOLQ1.csv"
    headers = ["maxPreds", "stock"]
else:
    if (questionNum == 2):
        file_name = "GOLQ2.csv"
        headers = ["predLifeLen", "foodEnergy"]
    else: #questionNum = 3
        file_name = "GOLQ3.csv"
        headers = ["maxPreds", "stock"]
dataFile = open(file_name, 'w')
line = ','.join(str(item) for item in headers)
dataFile.write(line + '\n')


trials = 5

for k in range(trials):
    j = 0
    # independent variable changing variables
    repoStockChange = 0


    # Question data collecting variables
    repoStock = 50
    stockGained = 1
    eatGain = 0
    


    if (questionNum == 1):
        numIter = 10
        repoStock = 10
        repoStockChange = 10
    else:
        if (questionNum == 2):
            numIter = 8
            stockGained = 0
            eatGain = 0.5
        else: #questionNum = 3
            numIter = 15

    # get data for different variables
    for j in range(numIter):
        i = 0
        maxPreds = 0
        print("Trial: ", k, "Iteration: ", j)
        stockGained += eatGain
        repoStock += repoStockChange
        
        #Empty array for the overall system state
        state = []

        #Add a list to track number of living cells per step
        records = []

        #Initializes a random selection of initially living cells
        start = 5000 # initial number of living cells
        side = 100 # there are 100 cells on each side of the grid (100x100 grid)

        births = [] # list that will hold the initial random cell location num for 5000 cells
        """
        file_path = '10x10.csv'
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()   
            
        for line in lines:
            row = line.strip()  # Split by comma, remove trailing newline
            num = int(row)
            births.append(num)

        """
        for i in range(start): # iterates over the 5000 cells to get a random location num 
            check = random.randint(0, side*side) # first try to get a unique cell location num
            while check in births: # keep trying again till you get a free cell
                check = random.randint(0, side*side)
            births.append(check) # add location num to the list

        predators = []

        #predators[{direction: 'v', negPos: -1, stockPile: 35, x: 0, y:0}]
        # Validation 1
        #predators = [{'direction': 'h', 'negPos': 1, 'stockPile': 10, 'x': 1, 'y':1, 'stepsLived':0}]

        # Validation 2
        #predators = [{'direction': 'v', 'negPos': -1, 'stockPile': 10, 'x': 1, 'y':1, 'stepsLived':0}]

        # Validation 3
        #predators = [{'direction': 'h', 'negPos': 1, 'stockPile': 20, 'x': 1, 'y':1, 'stepsLived':0}]

        # Validation 4
        #predators = [{'direction': 'h', 'negPos': 1, 'stockPile': 100, 'x': 1, 'y':1, 'stepsLived':0}]

        randX = random.randint(1, 98)
        randY = random.randint(1, 98)
        randDir = random.randint(1, 4)
        direct = "h"
        negPosDir = -1
        if (randDir % 2 == 1):
            direct = "v"
        if (randDir < 3):
            negPosDir = 1
        predators = [{'direction': direct, 'negPos': negPosDir, 'stockPile': repoStock, 'x': randX, 'y':randY, 'stepsLived':0}]
        
        print("Predator: ", direct, negPosDir, repoStock, randX, randY)

        #print(predators[0]['direction'])


        #Initializes system state based on RNG above
        for i in range(side):
            row = []
            for j in range(side):
                row.append(0)
                if i*side + j in births: # i is 100s place 
                    row[-1]=1 # switch to living
            state.append(row)
        """
        xcoord = predators[0]['x']
        ycoord = predators[0]['y']
        for k in range(3):
            for L in range(3):
                state[ycoord + k - 1][xcoord + L - 1] = 2
        """
        #predators[{direction: v, negPos: -1, stockPile: 35, x: 0, y:0}]


        living = [x for line in state for x in line if x == 1]
        records.append(len(living))

        if (seeVisuals == 1):
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 7), height_ratios = [3, 1])
            #Visualize the system state
            #Blue = Off
            #Yellow = On
            ax1.imshow(state)
            plt.ion()
            plt.show()
            plt.pause(2)
            ax2.plot(range(len(records)), records)
            
        lengthLivesList = []

        #Run the simulation for 250 steps, or until all dead
        for i in range(250):
            #Update the state based on Conway's rules
            state, lengthLife = gol.updateGoLstate(side, state, predators, repoStock, stockGained)
            lengthLivesList.extend(lengthLife)
                
            
            #calculate maxPreds
            numPreds = [pred for pred in predators if pred["stepsLived"] >= 3]
            numPredsNum = len(numPreds)
            if (numPredsNum > maxPreds):
                maxPreds = numPredsNum
            #print("num predators:               ", len(predators))
            if (len(predators) == 0):
                print("everyone died", i)
                break
            
            
            
            #Calculating number of living cells
            living = [x for line in state for x in line if x == 1]
            records.append(len(living))
            if (len(living)) == 0:
                break
            
            if (seeVisuals == 1):
                ax1.cla()
                ax1.imshow(state)
                plt.show(block=False)#prevents halt from plot
                plt.pause(0.001) #pause for human vision
                ax2.cla()
                ax2.plot(range(len(records)), records)
            
            # use if you need to see step-by-step eating
            """
            state = gol.updatePred(side, state, predators, repoStock)
            
            #Calculating number of living cells
            living = [x for line in state for x in line if x == 1]
            records.append(len(living))
            if (len(living)) == 0:
                break
                
            ax1.cla()
            ax1.imshow(state)
            plt.show(block=False)#prevents halt from plot
            plt.pause(0.2) #pause for human vision
            ax2.cla()
            ax2.plot(range(len(records)), records)
            """
        if (seeVisuals == 1):
            plt.ioff()
            plt.show()
        
        for pred in range(len(predators)):
            lengthLivesList.append(predators[pred]['stepsLived'])
        
        rows = gol.genDataRows(questionNum, state, predators, maxPreds, repoStock, stockGained, lengthLivesList)
        line = ','.join(str(item) for item in rows)
        dataFile.write(line + '\n')

if (seeVisuals == 1):
    plt.ioff()
    plt.show()
    #NOTE: the python code doesn't end until plot closed


