class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_right = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            prices[i], max_right = max_right- prices[i], max(max_right, prices[i])
        return 0 if max(prices) < 0 else max(prices)