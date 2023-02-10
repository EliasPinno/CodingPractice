n,s,k = input().split()
xs = [None] * n

for i in range(n):
    xs[i] = int(input())
xs = sorted(xs)
diffs = [None] * (n-1)
for i in range(n-1):
    diffs[i] = xs[i+1] - xs[i]
