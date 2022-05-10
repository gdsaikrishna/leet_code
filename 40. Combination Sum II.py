#39 -> 40 -> 77 -> 78 -> 90 -> 216
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(sorted(candidates), target, 0, [], res)
        return res
    
    def dfs(self, cdts, target, idx, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
        for i in range(idx, len(cdts)):
            if i > idx and cdts[i] == cdts[i-1]:
                continue
            self.dfs(cdts, target-cdts[i], i+1, path+[cdts[i]], res)