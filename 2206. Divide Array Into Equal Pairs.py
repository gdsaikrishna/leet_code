class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        for key in dic:
            if dic[key] % 2 == 1:
                return False
        return True
        