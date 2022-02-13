class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @lru_cache(None)
        def dfs(x, y1, y2):
            if y1 < 0 or y1 >= n or y2 < 0 or y2 >= n or x == m:
                return 0
            ans = grid[x][y1] + (y1 != y2) * grid[x][y2]
            ans += max(dfs(x + 1, y1 - 1, y2 - 1), dfs(x + 1, y1 - 1, y2), dfs(x + 1, y1 - 1, y2 + 1), \
                       dfs(x + 1, y1, y2 - 1), dfs(x + 1, y1, y2), dfs(x + 1, y1, y2 + 1), \
                       dfs(x + 1, y1 + 1, y2 - 1), dfs(x + 1, y1 + 1, y2), dfs(x + 1, y1 + 1, y2 + 1))
            return ans
        
        return dfs(0, 0, n - 1)