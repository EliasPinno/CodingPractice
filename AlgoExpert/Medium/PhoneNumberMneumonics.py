def phoneNumberMnemonics(phoneNumber):
    if len(phoneNumber) == 0:
        return []
    solution = []
    numTotalCombinations = 1
    for number in phoneNumber:
        numTotalCombinations *= len(DIGIT_LETTERS[int(number)])
    firstDigits = DIGIT_LETTERS[int(phoneNumber[0])]
    for digit in firstDigits:
        # Must be a whole number by definition
        for i in range(int(numTotalCombinations/len(firstDigits))):
            solution.append(digit)
    numToPlaceBeforeNextDigit = int(numTotalCombinations / len(firstDigits))
    for i in range(1, len(phoneNumber)):
        digitLetters = DIGIT_LETTERS[int(phoneNumber[i])]
        numDigits = len(digitLetters)
        numToPlaceBeforeNextDigit = int(numToPlaceBeforeNextDigit/numDigits)
        currentDigit = -1
        for j in range(numTotalCombinations):
            if j % numToPlaceBeforeNextDigit == 0:
                currentDigit += 1
            solution[j] = solution[j] + digitLetters[currentDigit % numDigits] 
    return solution

# O(4^n * n) time and space
# 4^n combos of n size to build (1 at a time) and store

DIGIT_LETTERS = {
    0: "0",
    1: "1",
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz"
}