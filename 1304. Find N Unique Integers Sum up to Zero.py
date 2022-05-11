class Solution:
    def sumZero(self, n: int) -> List[int]:
        k = n//2
        if n % 2 == 0:
            return list(range(-k, 0)) + list(range(1, k+1))
        else:
            return list(range(-k, k + 1))