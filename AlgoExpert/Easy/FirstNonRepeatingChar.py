def firstNonRepeatingCharacter(string):
    characterMap = {}
    for i in range(len(string)):
        char = string[i]
        characterMap[char] = i
    for i in range(len(string)):
        char = string[i]
        if char in characterMap:
            if characterMap[char] != i:
                del characterMap[char]
            else:
                return i
    return -1
# O(n) time (two passes) through the list
# O(1) space because there are only 26 characters in the alphabet for our input string
# However, it is more realistically O(k), where k is the size of the input "alphabet"