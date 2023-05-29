n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()

sum = arr[0]
idx = 1
while idx < n:
    if arr[idx]-1 != arr[idx-1]:
        sum += arr[idx]
    idx+=1
print(sum)