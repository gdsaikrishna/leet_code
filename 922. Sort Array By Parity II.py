class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        e, o = 0, 1
        
        while e<len(nums) and o<len(nums):
            if nums[e]%2==0:
                e+=2
            else:
                if nums[o]%2!=0:
                    o+=2
                else:
                    nums[e],nums[o] = nums[o],nums[e]
                    e+=2
                    o+=2
                                
        return nums