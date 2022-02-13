class Solution:
    def reverse(self, x: int) -> int:
        s = (x > 0) - (x < 0)
        x = int(str(x*s)[::-1])
        return s*x if x.bit_length() < 32 else 0