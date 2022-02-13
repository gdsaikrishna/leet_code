class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, currSum = nums[0], 0
        for ele in nums:
            if currSum < 0: currSum = 0
            currSum += ele
            maxSum = max(currSum, maxSum)
        
        return maxSum