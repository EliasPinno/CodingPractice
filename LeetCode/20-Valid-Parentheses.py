class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for i in range(len(s)):
            val_num = ord(s[i])
            if val_num in [40,91,123]: # Open bracket
                stack.append(val_num)
            else:
                if len(stack) != 0:
                    expected_num = stack.pop()
                    if val_num not in [expected_num+1,expected_num+2]:
                        return False
                else:
                    return False
        return len(stack) == 0

# Time: O(n)
# Space: O(n)