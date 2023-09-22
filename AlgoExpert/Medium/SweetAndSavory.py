def sweetAndSavory(dishes, target):
    # Write your code here.
    solution = [0,0]
    if len(dishes) < 2:
        return solution
    dishes.sort()
    sweetDishIdx = 0
    savoryDishIdx = len(dishes)-1
    print(sweetDishIdx)
    print(savoryDishIdx)
    closestValue = dishes[sweetDishIdx] + dishes[savoryDishIdx]
    while dishes[sweetDishIdx] < 0 and dishes[savoryDishIdx] > 0:
        currentSum = dishes[sweetDishIdx] + dishes[savoryDishIdx]
        if currentSum <= target and abs(currentSum - target) <= abs(closestValue - target):
            solution[0] = dishes[sweetDishIdx]
            solution[1] = dishes[savoryDishIdx]
            closestValue = currentSum
        if currentSum > target: # Dish is too savory: need less savory
            savoryDishIdx -= 1
        else:
            sweetDishIdx += 1
    return solution
# O(n) time, O(1) space