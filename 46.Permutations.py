class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [[n] + p
            for i, n in enumerate(nums)
            for p in self.permute(nums[:i] + nums[i+1:])] or [[]]

    # DFS
# def permute(self, nums):
#     res = []
#     self.dfs(nums, [], res)
#     return res
    
# def dfs(self, nums, path, res):
#     if not nums:
#         res.append(path)
#         # return # backtracking
#     for i in xrange(len(nums)):
#         self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)