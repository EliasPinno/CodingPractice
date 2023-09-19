def commonCharacters(strings):
    commonDict = {}
    numString = len(strings)
    for i in range(numString):
        string = strings[i]
        for char in string:
            if char not in commonDict:
                commonDict[char] = 1
            elif char in commonDict:
                if commonDict[char] == i:
                    commonDict[char] += 1
    solution = []
    print(commonDict)
    for key in commonDict.keys():
        if commonDict[key] == numString:
            solution.append(key)
    return solution
# O(k) space: there is a dictonary entry for every unique charcter across
# all of the strings. K is the total number of unique characters across
# all strings
# O(b) time, where b is the length of ALL strings combined