from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        if len(counts.values()) == len(set(counts.values())):
            return True
        return False