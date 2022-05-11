class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = second = 0
        for num in nums:
            first, second = max(first, num), max(second, min(first, num))
        return (first - 1)*(second - 1)