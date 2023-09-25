def maxSubsetSumNoAdjacent(values):
    if len(values) == 0:
        return 0
    if len(values) == 1:
        return values[0]
    n = len(values)
    bestSums = [-1]*n
    return max(getBestSumForPosition(0,n,values,bestSums),getBestSumForPosition(1,n,values,bestSums))

def getBestSumForPosition(i,n,values,sums):
    if i >= n:
        return 0
    if sums[i] != -1:
        return sums[i]
    sums[i] = values[i] + max(getBestSumForPosition(i+2,n,values,sums),getBestSumForPosition(i+3,n,values,sums))
    return sums[i]

# O(n) time, O(n) space