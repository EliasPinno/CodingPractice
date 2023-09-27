def sunsetViews(buildings, direction):
    isForward = direction == "WEST"
    correctRange = None
    if isForward: 
        correctRange = range(len(buildings))
    else:
        correctRange = range(len(buildings)-1, -1, -1)
    currentMaxBuilding = 0
    solution = []
    for i in correctRange:
        if buildings[i] > currentMaxBuilding:
            solution.append(i)
            currentMaxBuilding = buildings[i]
    if isForward:
        return solution
    return solution[::-1]
# O(n) time, O(n) space