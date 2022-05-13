class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        right = sum(nums)
        left = 0
        for i in range(len(nums)):
            left += nums[i]
            right -= nums[i]
            if left > right:
                return nums[0:i + 1]