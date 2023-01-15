class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        for right in range(1,len(prices)):
            if prices[right] < prices[left]:
                left = right
            max_profit = max(max_profit, prices[right] - prices[left])
        return max_profit
# O(n) time. No additional space required [O(n)].