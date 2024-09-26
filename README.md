[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/QIBFvvVe)
Piecewise Deterministic Markov Process (PDMP) Assignment
---

Consider a modification to Conway's Game of Life in which predators exist to "eat" the living cells.
The predator takes up the area of 9 cells.  It will consume cells overlapping with itself and which are within 1 cell outside of its body and stockpile the energy.
It can only move in one direction, but will turn around when it hits a wall.
In order to move, the predator must utilize some of its stockpiled energy.
If the stockpile reaches zero, the predator will die.
The death of a predator yields new cell life; the 9 cells previously occupied by the predator become a collection of 9 new living cells.
Predators reproduce through a random and inefficient splitting process based only on their stockpiled energy; children share the same locations as their parent for the first few moments of their life -- in the case of parental death, the children compete for food (first-born-first-served).
Once enough energy has been stockpiled, the predator chooses an offspring option from one of the following based on the provided probability distribution:
1. 35%: The predator lives and produces an offspring that moves inversely perpendicular to the parent (meaning: a parent moving in the positive vertical direction will have an offspring moving in the negative horizontal direction).  The predator shares 1/2 its stockpiled energy with its child.
2. 20%: The predator dies and produces two offspring that move in opposite directions perpendicular to the parent's motion.  Both offspring obtain 1/2 of the stockpiled energy from their parent.
3. 15%: The predator lives and produces an offspring that moves in the exact opposite direction to the parent's motion. The predator shares 1/2 its stockpiled energy with its child.
4. 30%: The predator dies and produces four offspring that all move in opposing directions. All offspring obtain 1/4 of the stockpiled energy from their parent.

The Task
---
Develop a simulation of this modification to the Game Of Life using the starting code in this repository, fully documenting your design, implementation, and testing.
Using a 100x100 grid and a set of 5000 randomly-distributed initial cells, generate datasets you'll analyze to answer the questions below.
Use an analysis strategy of your choice to produce figures that help to answer the questions, and include them in a version-controlled Markdown report of your findings that you'll post here.
Note that in order to answer the questions below, you'll need to make a variety of assumptions -- be sure to communicate these assumptions to your users.

Validating your simulation
---
The file 10x10.csv contains a set of initially living cells (0 is in the top-left corner, 1 is the cell immediately to its right, 10 is just below 0, and 99 is the bottom-right corner).  With no predators, the system begins at 40 living cells, and while it fluctuates throughout a 250-step observation period and falls at times below 30 living cells, the system seems to stay stable in the ballpark of 40 living cells.

- A predator with starting stockpile of 10 units, centered on cell 11, existing from the very first step of the simulation, moving in the positive horizontal direction, expending 5 units of energy per cell moved, and reproducing after amassing 50 units of energy at the cost of 15 units will perish as it hits the wall.
- A predator with starting stockpile of 10 units, centered on cell 11, existing from the very first step of the simulation, moving in the positive vertical direction (note: positive vertical direction is **down** due to the nature of the imshow visualization), expending 5 units of energy per cell moved, and reproducing after amassing 50 units of energy at the cost of 15 units will perish as it hits the bottom wall.
- A predator with starting stockpile of 20 units, centered on cell 11, existing from the very first step of the simulation, moving in the positive horizontal direction, expending 5 units of energy per cell moved, and reproducing after amassing 50 units of energy at the cost of 15 units will perish after it bounces off the right wall but before it touches the left wall again.
- A predator with starting stockpile of 100 units, centered on cell 11, existing from the very first step of the simulation, moving in the positive horizontal direction, expending 5 units of energy per cell moved, and reproducing after amassing 50 units of energy at the cost of 15 units will produce offspring on the second step of the simulation with outcome appropriate to the distribution given above.

Questions
---
1. How does the maximum number of predators suported by a system depend on how much stockpile is needed to reproduce in the predator lifecycle?
2. How does the length of a predator's life depend on the efficiency of its energy consumption (e.g., how many units of 'food' it gains per cell it 'eats')?
3. If the base rules of the Game of Life are changed, such that the cells have evolved to survive under conditions with 4 surrounding neighbors (but perish with 5 neighbors), does this increase or decrease the maximum number of predators which can be sustained in the system?

Rules
---
- This assignment is to be individually submitted, but you are welcome to collaborate with others provided you are not looking at each others code.  Describing behaviors, devising strategy, developing documentation, etc. may certainly be collaborated on with no restrictions.  The goal here is to ensure that everyone is able to carry a coding task forward on their own during the final project.  Use your best judgement about how you want to offer help to your peers -- the grade on this assignment is unimportant compared to the final project, and preventing someone from struggling now and learning to be an effective, independent developer affects the dynamics of the final project teams.
- You are welcome to seek help from any online resource, any friend (in the course or not), any AI which you might use to generate code, etc. **IF AND ONLY IF** you properly cite all resources you use.
- This assignment is intended to push each of you, regardless of python ability.  Some of you will make it farther through this assignment than others, and the grading scheme will be flexible.  Every student must make realistic progress on the tasks above by October 10.  Past that point, I will allow for penalty-free late submissions up to October 24 **IF AND ONLY IF** your realistic attempt meets minimum course expectations.
- PAL is not a valid resource for a 300-level course.  You may find me during office hours on Wednesdays, or reach out via the Teams space for asynchronous help.
