class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = list(str(n))
        prod, add = 1, 0
        for i in digits:
            prod *= int(i)
            add += int(i)
        return prod - add