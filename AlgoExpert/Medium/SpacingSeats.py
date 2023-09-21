import math

def bestSeat(seats):
    maxZeroes = 0
    currentZeroes = 0
    currentBestIndex = -1
    for i in range(len(seats)):
        if seats[i] == 1:
            if currentZeroes > maxZeroes:
                maxZeroes = currentZeroes
                if maxZeroes % 2 == 1:
                    currentBestIndex = i - math.ceil(maxZeroes/2)
                else:
                    currentBestIndex = i - math.ceil(maxZeroes/2) - 1
                currentZeroes = 0
            else:
                currentZeroes = 0
        else:
            currentZeroes += 1
    return currentBestIndex
# O(n) time, O(1) space