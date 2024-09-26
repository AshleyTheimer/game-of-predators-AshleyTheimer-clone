#Conway's Game Of Life
#Author: RR & CIS343-F24
#Last Updated: 9/24/2024

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
start = 3000
side = 100

births = []
for i in range(start):
    check = random.randint(0, side*side)
    while check in births:
        check = random.randint(0, side*side)
    births.append(check)

#Initializes system state based on RNG above
for i in range(side):
    row = []
    for j in range(side):
        row.append(0)
        if i*side + j in births:
            row[-1]=1
    state.append(row)

living = [x for line in state for x in line if x == 1]
records.append(len(living))

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 7), height_ratios = [3, 1])

#Visualize the system state
#Blue = Off
#Yellow = On
ax1.imshow(state)
plt.ion()
plt.show()
ax2.plot(range(len(records)), records)

#Run the simulation for 250 steps, or until all dead
for i in range(250):
    #Update the state based on Conway's rules
    state = gol.updateGoLstate(state)
    
    #Calculating number of living cells
    living = [x for line in state for x in line if x == 1]
    records.append(len(living))
    if (len(living)) == 0:
        break
        
    ax1.cla()
    ax1.imshow(state)
    plt.show(block=False)#prevents halt from plot
    plt.pause(0.1) #pause for human vision
    ax2.cla()
    ax2.plot(range(len(records)), records)

plt.ioff()
plt.show()
#NOTE: the python code doesn't end until plot closed


