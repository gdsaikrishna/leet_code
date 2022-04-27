class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [None for i in range(len(indices))]
        for i, c in enumerate(indices):
            ans[c] = s[i]
        return ''.join(ans)