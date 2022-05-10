class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans, dic = 0, defaultdict(int)
        for num in nums:
            dic[num] += 1
        for key in dic:
            if key - k in dic:
                ans += dic[key]*dic[key-k]
        return ans
            