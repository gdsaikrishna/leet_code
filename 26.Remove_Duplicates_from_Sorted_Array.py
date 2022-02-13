class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        pos, curr = 1, nums[0]
        for i in range(1, len(nums)):
            if nums[i] != curr:
                nums[pos], curr = nums[i], nums[i]
                pos+=1
        return pos