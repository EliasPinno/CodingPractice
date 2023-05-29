n, d = map(int, input().split())
arr = [int(i) for i in input().split()]
arr.sort()
divArr = [i//d for i in arr]
startIdx = 0
currentVal = divArr[0]
for i in range(1,n):
    if divArr[i] != currentVal:
        if startIdx != i-1:
            