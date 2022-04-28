class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        grid = heights
        # edge cases:
        if not grid:
            return 0

        from heapq import heappush, heappop
        h = [(0, (0,0))] # key to heap is cost
        costSoFar = {(0,0): 0} 
        dirs = [(1,0), (0,1), (-1,0), (0,-1)] # all 4 dirs
        trgt = (len(grid)-1, len(grid[0])-1) 
        import math
        maxDelta = 0 # -------- [*]
        while h:
            cost, node = heappop(h)
            maxDelta = max(maxDelta, cost) # -------- [*]
            x, y = node
            if node == trgt: # - Dijkstra can have early terminate
                break

            for dir in dirs:
                newX, newY = x+dir[0], y+dir[1]

                if newX >= 0 and newX <= len(grid)-1 and newY >= 0 and newY <= len(grid[0])-1:

                    edgeCost = abs(grid[x][y] - grid[newX][newY]) # ------- [*]

                    if (newX, newY) not in costSoFar or ( (newX, newY) in costSoFar and edgeCost < costSoFar[(newX, newY)]):
                        costSoFar[(newX, newY)] = edgeCost
                        heappush(h, (edgeCost, (newX, newY)))

        return maxDelta # -------- [*]