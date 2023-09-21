def threeNumberSum(array, targetSum):
    array.sort()
    solution = []
    for i in range(len(array)-2):
        currentTarget = targetSum - array[i]
        left = i+1
        right = len(array) - 1
        while left < right:
            currentSum = array[left] + array[right]
            if  currentSum == currentTarget:
                solution.append([array[i], array[left], array[right]])
            if currentSum > currentTarget:
                right -= 1
            else:
                left += 1
    return solution
# O(n) space (every number in array could be in a triplet)
# O(n^2) time (n n/2 iterations)
