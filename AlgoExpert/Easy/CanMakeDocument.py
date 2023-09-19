def generateDocument(characters, document):
    charactersMap = getCharMapFromString(characters)
    documentMap = getCharMapFromString(document)
    for key in documentMap.keys():
        if key not in charactersMap:
            return False
        elif charactersMap[key] < documentMap[key]:
            return False
    return True

def getCharMapFromString(string):
    charMap = {}
    for char in string:
        if char not in charMap:
            charMap[char] = 1
        else:
            charMap[char] += 1
    return charMap
# O(n+m) time where n is the number of characters in chars, m in document
# O(i+j) space where i distinct char in chars, j in document 
# More efficent solution: don't generate map for document, and just subtract
# from charMap