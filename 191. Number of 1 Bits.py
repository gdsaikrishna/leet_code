class Solution:
    def hammingWeight(self, n: int) -> int:
        print(n)
        return bin(n).count('1')