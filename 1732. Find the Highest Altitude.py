class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans, tracker= 0, 0
        for g in gain:
            tracker += g
            ans = max(ans, tracker)
        return ans