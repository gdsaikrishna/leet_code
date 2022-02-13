class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ans, last = 0, -1
        for i, seat in enumerate(seats):
            if seat:
                ans = max(ans, (i-last)//2 if last >=0 else i)
                last = i
        return max(ans, len(seats) - 1 - last if not seats[-1] else 0)