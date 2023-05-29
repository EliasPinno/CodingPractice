class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_data = list(enumerate(nums))
        sorted_data = sorted(indexed_data, key=lambda x: x[1])
        sorted_values = [x[1] for x in sorted_data]
        sorted_indices = [x[0] for x in sorted_data]
        for i in range(0, len(nums)):
            localTarget = target - sorted_values[i]
            for j in range(len(nums)-1, i, -1):
                if sorted_values[j] == localTarget:
                    return [sorted_indices[i], sorted_indices[j]]
        return None
# O(nlogn) time, O(n) space (but about 4n). Very inefficient as a solution, going to redo with dict
