class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int('1'*(n.bit_length()), 2) ^ n if n > 0 else 1