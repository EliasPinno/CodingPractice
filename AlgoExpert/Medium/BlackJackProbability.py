def blackjackProbability(target, startingHand):
    return blackjackProbabilityRecursive(target, startingHand, {})
# Probability is: all the way

def blackjackProbabilityRecursive(target, startingHand, memory):
    if startingHand in memory:
        return memory[startingHand]
    if startingHand > target:
        return 1.0
    if startingHand <= target and startingHand >= target - 4:
        return 0.0
    probToBust = 0
    for i in range(1,11):
        probToBust += 0.1 * blackjackProbabilityRecursive(target, startingHand + i, memory)
    memory[startingHand] = probToBust
    return probToBust
# O(target - start) time, space 