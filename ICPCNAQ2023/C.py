s1 = input()
s2 = input()

s1p = 0
s2p = 0

solution = ""

while s1p < len(s1) or s2p < len(s2):
    if s1p == len(s1):
        solution += s2[s2p]
        s2p += 1
    elif s2p == len(s2):
        solution += s1[s1p]
        s1p += 1
    elif ord(s1[s1p]) < ord(s2[s2p]):
        solution += s1[s1p]
        s1p += 1
    else:
        solution += s2[s2p]
        s2p += 1
print(solution)