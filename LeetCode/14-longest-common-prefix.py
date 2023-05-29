class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        currentPrefixLength = 0
        keepGoing = True
        while keepGoing:
            if currentPrefixLength >= len(strs[0]):
                break
            goalChar = strs[0][currentPrefixLength]
            for i in range(1, len(strs)):
                if currentPrefixLength >= len(strs[i]) or strs[i][currentPrefixLength] != goalChar:
                    keepGoing = False
                    break
            if keepGoing:
                currentPrefixLength += 1

        return strs[0][0:currentPrefixLength]
# O(nk) where n is number of strings, and k is the length of the longest string in the sequence.

            