from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        arr_dict = Counter(arr)
        for key, value in arr_dict.items():
            if value == 1:
                k -= 1
                if not k:
                    return key
        return ''