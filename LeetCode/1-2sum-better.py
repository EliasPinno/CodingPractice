class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, val in enumerate(nums):
            if val in d:
                return [idx,d[val]]
            localTarget = target - val
            d[localTarget] = idx
        return None

# O(n) time, O(n) space? Much better solution then previous one.