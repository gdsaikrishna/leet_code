class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []
        less_count, equal_count = 0, 0
        for num in nums:
            if num < target:
                less_count+=1
            elif num == target:
                equal_count += 1
            else:
                pass
        if equal_count != 0:
            ans = [less_count+ i  for i in range(equal_count)]
        return ans
        