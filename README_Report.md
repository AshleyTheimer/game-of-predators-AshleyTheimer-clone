### Testing
1) To first validate my predators movement in my program, I used the constraints set in the validation step 1 to compare my results of my program with the intended results of the validation.
    - I also separated the state updates between the original game of life (living and dead cells) updates and the predator updates to count and validate how many cells the predator was eating.
    - I slowed down the framerate to ensure the bounces off of the wall didn't occur at the wrong position. (that the 3x3 predator kept its shape throughout the bounce)
2) I validated the movements and deaths of the predators with the validation steps 1-3
3)  I then added the reproducing function and only used the first reproduce option to test that it worked properly. I used the constraints of validation step 4 and compared the results of that to the sim results, since it was the only validation step that included reproduction,
4)  To validate that reproduction option 4 worked properly, I used the constraints of validation step 4 and moved the starting position of the preditor cell to the center of the grid and observed that all 4 offspring moved in separate directions.
