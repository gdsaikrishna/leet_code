class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dic, ans = defaultdict(int), 0
        for num in nums:
            dic[num]+=1
        for key in dic:
            if dic[key] == 1:
                ans += key
        return ans