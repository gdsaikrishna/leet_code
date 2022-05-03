class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols, perimeter = len(grid), len(grid[0]), 0
        
        for m in range(rows):
            for n in range(cols):
                if grid[m][n] == 1:
                    perimeter += 4
                    #top edge condition
                    if m!= 0 and grid[m-1][n] == 1: perimeter -= 1
                    #left edge condition
                    if n!= 0 and grid[m][n-1] == 1: perimeter -= 1
                    #bottom edge condition
                    if m != rows - 1 and grid[m+1][n] == 1: perimeter -= 1
                    #right edge condition
                    if n != cols - 1 and grid[m][n+1] == 1: perimeter -= 1
        return perimeter