class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clean the string into it's more proper form
        sClean = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if len(sClean) < 2:
            return True
        for i in range(math.ceil(len(sClean)/2)):
            if sClean[i] != sClean[len(sClean)-1-i]:
                return False
        return True
# O(n) space, O(n) time