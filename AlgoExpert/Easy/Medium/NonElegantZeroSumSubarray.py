def zeroSumSubarray(nums):
    n = len(nums)
    if n == 0:
        return False
    prefixSums = [0]*n
    prefixSums[0] = nums[0]
    for i in range(1, len(nums)):
        prefixSums[i] = nums[i] + prefixSums[i-1]
    foundSums = set()
    for sum in prefixSums:
        if sum in foundSums or sum == 0:
            return True
        else:
            foundSums.add(sum)
    return False
# O(n) time, O(n) space