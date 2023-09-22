def oneEdit(stringOne, stringTwo):
    oneLength = len(stringOne)
    twoLength = len(stringTwo)
    if abs(oneLength - twoLength) > 1:
        return False
    if oneLength == twoLength:
        return canReplace(stringOne,stringTwo) # handles identical as well
    # If str + add = str2, then str2 - add = str 1
    pointer1 = 0
    pointer2 = 0
    diffs = 0
    while pointer1 < oneLength and pointer2 < twoLength:
        if stringOne[pointer1] != stringTwo[pointer2]:
            diffs += 1
            if diffs > 1:
                return False
            if oneLength < twoLength:
                pointer2 += 1
                continue
            else:
                pointer1 += 1
                continue
        pointer1 += 1
        pointer2 += 1
    return True
    
def canReplace(stringOne, stringTwo):
    diffs = 0
    for i in range(len(stringOne)):
        if stringOne[i] != stringTwo[i]:
            diffs += 1
            if diffs > 1:
                return False
    return True
# O(n+m) time, O(1) space