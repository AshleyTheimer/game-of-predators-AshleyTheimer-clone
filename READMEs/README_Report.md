### Validation
1) To first validate my predators movement in my program, I used the constraints set in the validation step 1 to compare my results of my program with the intended results of the validation.
    - I also separated the state updates between the original game of life (living and dead cells) updates and the predator updates to count and validate how many cells the predator was eating.
    - I slowed down the framerate to ensure the bounces off of the wall didn't occur at the wrong position. (that the 3x3 predator kept its shape throughout the bounce)
2) I validated the movements and deaths of the predators with the validation steps 1-3
3)  I then added the reproducing function and only used the first reproduce option to test that it worked properly. I used the constraints of validation step 4 and compared the results of that to the sim results, since it was the only validation step that included reproduction,
4)  To validate that reproduction option 4 worked properly, I used the constraints of validation step 4 and moved the starting position of the preditor cell to the center of the grid and observed that all 4 offspring moved in separate directions.
5)  To validate that my reproduction distribution was working properly, I would check how many times each reproduction option was chosen and see if each option was chosen roughly the percentage of times that was described in the distribution, which it was.

### Verification
1) The only graph I needed to verify was working properly was the graph for question 2. At first, the graph came out with results that showed no correlation whatsoever, which based upon my hypothesis, definately should have. Next I thought about the compounding variables, and remembered that some of the reproduction options made the parent die instantly upon reproduction. I then fixed my functions to take into account the amount of stock the predators were gaining to make the reporoduction more even accross all the different simulations, because, the numerous instantaneous deaths was throwing off my investigation and data.
2) When I needed to see my simulation behavior properly, I looked at the simulation step by step to make sure everything was moving as it should.
3) For question 3, I verified that the simulation was moving as it should by showing figures of the simulation side by side and comparing the results as the simulation moved very slowly.
