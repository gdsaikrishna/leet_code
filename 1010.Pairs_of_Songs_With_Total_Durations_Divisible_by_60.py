from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic, ans = defaultdict(int), 0
        for duration in time:
            rem = duration % 60
            ans += dic[0] if rem == 0 else dic[60-rem]
            dic[rem] += 1
        return ans