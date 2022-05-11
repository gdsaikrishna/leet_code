class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        last = start + 2 * (n - 1)
        if start % 4 < 2:
            start = 0
        else:
            n -= 1
        if n % 2 == 0: return start ^ (n & 2)
        return start ^ last ^ (n & 2)