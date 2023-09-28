def longestPalindromicSubstring(string):
    maxString = string[0]
    for i in range(len(string)):
        currentString = extendPalindromeFromCenter(string, i)
        print("{} has currentString: {}.".format(i,currentString))
        if len(currentString) > len(maxString):
            maxString = currentString
    return maxString

def extendPalindromeFromCenter(string, i):
    even = extendPalindromeFromCenterHelper(string, i, i+1)
    odd = extendPalindromeFromCenterHelper(string, i, i)
    if len(even) > len(odd):
        return even
    return odd

def extendPalindromeFromCenterHelper(string, i1, i2):
    left = i1
    right = i2
    while isCharEqual(string, left, right):
        left -= 1
        right += 1
    return string[left+1:right]

def isCharEqual(string, i1, i2):
    if i1 < 0 or i2 >= len(string):
        return False
    return string[i1] == string[i2]
# O(n) space, O(n^2) time