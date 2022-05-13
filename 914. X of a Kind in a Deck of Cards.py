class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) <= 1:
            return False
        counts = list(Counter(deck).values())
        gcd_val = counts[0]
        for value in counts:
            gcd_val = math.gcd(gcd_val, value)
        return True if gcd_val != 1 else False