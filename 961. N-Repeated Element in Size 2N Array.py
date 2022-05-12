class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                return num
        return 0