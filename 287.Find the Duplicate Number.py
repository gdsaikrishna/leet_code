class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Convert number to -ve based on traversal. If an index is visited twice then it is the duplicate
        for num in nums:
            indx = abs(num)
            if nums[indx] > 0 :
                nums[indx] *= -1
            else:
                return indx