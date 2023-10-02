def selectionSort(array):
    # Write your code here.
    n = len(array)
    for i in range(n):
        minVal = array[i]
        minIdx = i
        for j in range(i+1, n):
            if array[j] < minVal:
                minVal = array[j]
                minIdx = j
        array[i], array[minIdx] = array[minIdx], array[i]
    return array
# O(n^2) time O(1) space