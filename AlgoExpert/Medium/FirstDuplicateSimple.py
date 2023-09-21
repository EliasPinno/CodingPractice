def firstDuplicateValue(array):
    frequencyMap = {}
    for value in array:
        if value in frequencyMap:
            return value
        frequencyMap[value] = True
    return -1
# O(n) time, O(n) space