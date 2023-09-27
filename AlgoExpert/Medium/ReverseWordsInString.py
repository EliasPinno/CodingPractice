def reverseWordsInString(string):
    if len(string) == 0:
        return ""
    solution = []
    addingSpaces = string[-1] == " "
    currentElemEnd = len(string)-1
    for i in range(len(string)-1, -1, -1):
        currentChar = string[i]
        charIsSpace = currentChar == " "
        if charIsSpace != addingSpaces:
            solution.append(string[i+1:currentElemEnd+1])
            currentElemEnd = i
            addingSpaces = not addingSpaces
    solution.append(string[0:currentElemEnd+1])
    return "".join(solution)
# O(n) time, O(n) space