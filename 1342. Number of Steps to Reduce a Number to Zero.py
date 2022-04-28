class Solution:
    def numberOfSteps(self, num: int) -> int:
        binary = bin(num)[2:]
        return len(binary) -1 + binary.count('1')
        