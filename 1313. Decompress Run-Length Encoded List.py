class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)//2):
            for j in range(nums[2*i]):
                ans.append(nums[2*i+1])
        return ans