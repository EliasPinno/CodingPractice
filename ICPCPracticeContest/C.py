def getHIndex(arr: list[int], n: int):
    arr.sort()
    idx = 0
    currentMaxHCount = n
    while idx < n:
        if arr[idx] >= currentMaxHCount:
            return currentMaxHCount
        idx += 1
        currentMaxHCount -= 1
    return 0

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
print(getHIndex(arr,n))