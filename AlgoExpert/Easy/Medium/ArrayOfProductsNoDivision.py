# O(n) time: 3 linear passes over array
# O(n) space: 3 n sized arrays
def arrayOfProducts(array):
    n = len(array)
    if n == 1:
        return [1]
    rightProducts = [0]*n
    leftProducts = [0]*n
    rollingProduct = 1
    for i in range(n-1):
        leftProducts[i] = rollingProduct*array[i]
        rollingProduct = leftProducts[i]
    rollingProduct = 1
    for i in range(n-1, 0, -1):
        rightProducts[i] = rollingProduct*array[i]
        rollingProduct = rightProducts[i]
    solution = [0]*n
    solution[0] = rightProducts[1]
    solution[n-1] = leftProducts[n-2]
    for i in range(1,n-1):
        solution[i] = leftProducts[i-1]*rightProducts[i+1]
    return solution
