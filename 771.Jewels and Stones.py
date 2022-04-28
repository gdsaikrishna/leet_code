class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_dict = defaultdict(int)
        for i in stones:
            stone_dict[i] +=1
        res = 0
        for i in jewels:
            if i in stone_dict:
                res+= stone_dict[i]
        return res