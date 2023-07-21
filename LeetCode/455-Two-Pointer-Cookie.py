class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        totalSatisfied = 0
        gPointer = len(g) - 1
        sPointer = len(s) - 1
        while sPointer >= 0 and gPointer >= 0:
            if s[sPointer] >= g[gPointer]:
                totalSatisfied += 1
                sPointer -= 1
                gPointer -= 1
            else:
                gPointer -= 1
        return totalSatisfied 
# O(glogg + slogs) time since we sort g and s, where g and s are the size of the 
# different lists respectively. Space is O(g/s) where g and s are all of the values we have to read