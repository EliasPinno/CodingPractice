def runLengthEncoding(string):
    # Write your code here.
    newOutput = []
    prevChar = string[0]
    currentCharCount = 1
    for i in range(1, len(string)):
        currentChar = string[i]
        if currentChar == prevChar and currentCharCount < 9:
            currentCharCount += 1
        else:
            newOutput.append(str(currentCharCount))
            newOutput.append(prevChar)
            prevChar = currentChar
            currentCharCount = 1
    newOutput.append(str(currentCharCount))
    newOutput.append(prevChar)
    return ''.join(newOutput)

# O(n) time, O(n) space
