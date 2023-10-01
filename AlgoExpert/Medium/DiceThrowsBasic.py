def diceThrows(numDice, numSides, target):
    memory = [[-1 for _ in range(target+1)] for _ in range(numDice+1)]
    print(memory)
    return diceThrowsRecursive(numDice, numSides, target, memory)

def diceThrowsRecursive(numDice, numSides, target, memory):
    if numDice == 0 or target < 0:
        if target == 0:
            return 1
        return 0
    elif memory[numDice][target] != -1:
        return memory[numDice][target]
    else:
        numWaysToReach = 0
        for i in range(1,numSides+1):
            numWaysToReach += diceThrowsRecursive(numDice-1, numSides, target-i,memory)
    memory[numDice][target] = numWaysToReach
    return numWaysToReach
