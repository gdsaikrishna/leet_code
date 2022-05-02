class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        res, start, end = [], nums[0], nums[0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                end = nums[i]
            else:
                ans = str(start)+"->"+str(end) if start != end else str(start)
                res.append(ans)
                start, end = nums[i], nums[i] 
        ans = str(start)+"->"+str(end) if start != end else str(start)
        res.append(ans)
        return res