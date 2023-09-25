def staircaseTraversal(height, maxSteps):
    memory = (height+1)*[-1]
    memory[0] = 1
    memory[1] = 1
    return returnNumStepsForHeight(height,maxSteps,memory)

def returnNumStepsForHeight(height,maxSteps,memory):
    if height < 0:
        return 0
    if memory[height] != -1: # We explored this before
        return memory[height]
    totalForSpot = 0
    for i in range(1,maxSteps+1):
        totalForSpot += returnNumStepsForHeight(height-i,maxSteps,memory)
    memory[height] = totalForSpot
    return totalForSpot
# O(n*k) time, O(n) space.