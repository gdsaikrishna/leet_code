class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pair_map, operations = defaultdict(int), 0
        for num in nums:
            #If pair found increment operations
            if pair_map[num]:
                operations += 1
                pair_map[num] -= 1
            else:
                pair_map[k- num] += 1
        return operations