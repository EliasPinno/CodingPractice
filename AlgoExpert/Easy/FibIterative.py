def getNthFib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    lastTwoValues = [0,1]
    iterations = n-2
    currentVal = 0
    while iterations > 0:
        currentVal = lastTwoValues[0] + lastTwoValues[1]
        lastTwoValues[0] = lastTwoValues[1]
        lastTwoValues[1] = currentVal
        iterations -= 1
    return currentVal
# O(n) time, O(1) space
# Since array never grows above 2 size.