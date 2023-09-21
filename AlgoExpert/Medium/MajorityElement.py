def majorityElement(array):
    currentMajority = array[0]
    longestRepeat = 1
    currentRepeat = 1
    currentChar = array[0]
    for i in range(1,len(array)):
        if array[i] == array[i-1]:
            currentRepeat += 1
            if currentRepeat > longestRepeat:
                longestRepeat = currentRepeat
                currentMajority = currentChar
        else:
            currentChar = array[i]
            currentRepeat = 1
    return currentMajority
# O(n) time, O(1) space
# Principle: by definiton, majority must have longest string of repetitions 
# Default value covers case like [3,1,3,1,3]
