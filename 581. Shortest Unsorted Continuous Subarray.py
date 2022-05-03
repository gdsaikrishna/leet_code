class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n, start, end = len(nums), 0, len(nums)-1
        
        while start < n-1 and nums[start] <= nums[start+1]:
            start += 1
        
        if start == n-1 : return 0
        
        while end > 0 and nums[end] >= nums[end -1]:
            end -= 1
        
        tempMin, tempMax = min(nums[start:end+1]), max(nums[start: end+1])
        
        while start > 0 and nums[start -1] > tempMin:
            start -= 1
            
        while end < n-1 and nums[end + 1] < tempMax:
            end += 1
        
        return end - start + 1
        