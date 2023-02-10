def taxi(n):
    return 1 + 2*(n*(n+1))

def spidey(n):
    return taxi(n) + max(0,4*(n-2))

def spideyHelper(n):
    if n % 2 == 0:
        
    else:


n, m = input().split()

print(taxi(int(n)))
print(spidey(int(m)))
print("break")
for i in range(8):
    print(taxi(i))