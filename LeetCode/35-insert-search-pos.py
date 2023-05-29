class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        if target < nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)
        while right >= left:
            search = (right+left)//2
            #print(f"Left is: {left}, Right is: {right}, Search is: {search}")
            if nums[search] == target:
                return search
            elif nums[search] < target:
                left = search + 1
            else:
                right = search -1
        return left
