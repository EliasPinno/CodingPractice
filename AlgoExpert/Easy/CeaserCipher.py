def caesarCipherEncryptor(string, key):
    # Make the string a list for easier modification
    stringList = list(string)
    solutionList = list(map(lambda c: ceaserCipherSingleChar(c,key), stringList))
    return ''.join(solutionList)

def ceaserCipherSingleChar(char, key):
    charNumber = ord(char)
    alphabetValue = charNumber - 97
    alphabetValue = (alphabetValue + key) % 26
    finalValue = alphabetValue + 97
    return chr(finalValue)

# O(n) time where n is length of the input string (operation only on
# each character.)
# O(n) space since we are returning a new string