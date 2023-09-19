def semordnilap(words):
    pairMap = {}
    solution = []
    for word in words:
        if word in pairMap:
            pairMap[word] = word[::-1]
        else:
            pairMap[word[::-1]] = -1
    for key, value in pairMap.items():
        if value != -1:
            solution.append([key,value])
    # Write your code here.
    return solution
# O(n) time where n is the number of words
# O(n) space where n is the number of words