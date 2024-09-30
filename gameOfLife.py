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

#Empty array for the overall system state
state = []

#Add a list to track number of living cells per step
records = []

#Initializes a random selection of initially living cells
start = 5000 # initial number of living cells
side = 10 # there are 100 cells on each side of the grid (100x100 grid)

births = [] # list that will hold the initial random cell location num for 5000 cells

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
"""

#predators[{direction: 'v', negPos: -1, stockPile: 35, x: 0, y:0}]
# Validation 1
predators = [{'direction': 'h', 'negPos': 1, 'stockPile': 10, 'x': 1, 'y':1}]

# Validation 2
#predators = [{'direction': 'v', 'negPos': -1, 'stockPile': 10, 'x': 1, 'y':1}]
print(predators[0]['direction'])


#Initializes system state based on RNG above
for i in range(side):
    row = []
    for j in range(side):
        row.append(0)
        if i*side + j in births: # i is 100s place 
            row[-1]=1 # switch to living
    state.append(row)

state, energyGain = gol.eat(side, state, predators, 0)
predators[0]['stockPile'] += energyGain

xcoord = predators[0]['x']
ycoord = predators[0]['y']
for k in range(3):
    for L in range(3):
        state[ycoord + k - 1][xcoord + L - 1] = 2

#predators[{direction: v, negPos: -1, stockPile: 35, x: 0, y:0}]


living = [x for line in state for x in line if x == 1]
records.append(len(living))

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 7), height_ratios = [3, 1])

#Visualize the system state
#Blue = Off
#Yellow = On
ax1.imshow(state)
plt.ion()
plt.show()
plt.pause(2)
ax2.plot(range(len(records)), records)


#Run the simulation for 250 steps, or until all dead
for i in range(25):
    #Update the state based on Conway's rules
    state = gol.updateGoLstate(side, state, predators)
    
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
    
    # use if you need to see step-by-step eating
    """
    state = gol.updatePred(side, state, predators)
    
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

plt.ioff()
plt.show()
#NOTE: the python code doesn't end until plot closed


