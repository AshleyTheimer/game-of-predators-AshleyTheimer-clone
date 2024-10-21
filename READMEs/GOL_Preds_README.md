gameOfLife.py and gameOfLifeQ3_1.py are Python files that simulates a game of life with predators that eat living cells for 250 steps and collects data based on the users input.
## Key Feature
- code builds a random initial state of a 100x100 grid that has half of the initial cells living, and the other hald dead
## Getting Started
These instructions will help Windows users properly install and run the program:
- Imports
  - functions.py or functionsQ2.py for gameOfLife.py
  - functionsQ3_1.py for gameOfLifeQ3_1.py
- Usage:
  - user must define which question they are trying to solve on line 24. They must choose either 1 or 2 (gameOfLifeQ3_1.py answers question 3 without the user having to change this number)
  - User can change how many trials they will perform to collect data on line 44 of gameOfLife.py or line 30 on gameOfLifeQ3_1.py
## How the program works:
- both programs set up the initial game of life states and spawns in a predator. The files use 3 loops.
  1) Innermost: updates the current simulation of the game of life
  2) Middle: Runs the simulation through different variable numbers
  3) Outer: Runs those simulations a bunch of times to get multiple trials
- The function files takes care of updating the simulations state, including which cells are living, dead or predators. It also takes care of reproducing predators and the death of predators
- Data will be collected in a csv file:
    - 'GOLQ1.csv' for question 1. copy the data into 'GOLQ1Accum.csv' to graph later with GOLQ1Graph.py
    - 'GOLQ2.csv' for question 2. copy the data into 'GOLQ2Accum.csv' to graph later with GOLQ2Graph.py
    - 'GOLQ3.csv' for question 3. copy the data into 'GOLQ1not.csv' to graph later with GOLQ3Graph.py -- this is on gameOfLifeQ3_1.py

## Data Flow Diagram
The data flow diagram shows how data moves through a system. A good data flow diagram can show what a system does, what goes in, what comes out, and where it all goes. This is a much easier way to portray the movement of data than text is. Rules of a data flow diagram are as follows: 
- [] Circle - represents processes.
- [] Box – represents external data.
- [] Text within two lines – represents data storage.
- [] Arrow – represents data flow. 
Using these simple signifiers in a data flow diagram is an easy and effective way to show how data moves through a specific system. 

    In this Shakespeare assignment, “Shakespeare.txt” is a data storage that has data of all of Shakespeare’s work. From here data flows to a system file “cleaning” process through using the file path of “shakspeare.txt”. This data then flows to another data storage of a list of sonnets. External data of a user inputted word is validated then passed into the frequency generation process. From here, the system counts word frequency. This is represented as a circle in the data flow diagram because this is a process. A frequency list is then generated. The combination of the user’s entered word and this list automatically generates the next word that is produced. From here, a sonnet is fully generated using the process of generating a lot of next words. Also at this step, a data storage containing a list of bad endings checks the sonnet, making sure the sonnet doesn’t use one of the words in the list at the end of the sonnet. Next, the sonnet is printed. Users then have an option to save the sonnet, where it would be stored in a data storage called “saved sonnets”. If not users can continue by inputting a new word or ending the system. If they would like to continue using the system, users can input a new word, which would be validated and goes through the same processes as it did early in the diagram. If they would like to end the system, users are taken to an external data source of returned sonnets. Data flow diagrams are extremely helpful to the overall understanding of how a system works and is an easy way for users to follow along. 

