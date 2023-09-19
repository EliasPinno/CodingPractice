def generateDocument(characters, document):
    charMap = {}
    for char in characters:
        if char not in charMap:
            charMap[char] = 1
        else:
            charMap[char] += 1
    for char in document:
        if char not in charMap or charMap[char] == 0:
            return False
        charMap[char] -= 1
    return True
# O(n+m) time where n is the number of characters in chars, m in document
# O(i) space where i distinct char in chars
# More efficent solution: don't generate map for document, and just subtract
# from charMap