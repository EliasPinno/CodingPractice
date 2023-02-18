class Solution:
    def rob(self, nums: List[int]) -> int:
        self.costs = {}
        return self.robR(nums,0)

    def robR(self, nums: List[int], index: int) -> int:
        if index >= len(nums):
            return 0
        if index not in self.costs:
            self.costs[index] = max(nums[index]+self.robR(nums,index+2), self.robR(nums,index+1))
        return self.costs[index]
# O(n) space, O(n) time