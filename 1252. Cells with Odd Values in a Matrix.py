class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        # Keep track of all increments to rows, columns in lists(i.e row_val, col_val)
        # Get a particular (i,j) cell value by :
        # sum of increments of row(i.e row_val[i]) +  increments of column(i.e col_val[j])
        row_val, col_val = [0]*m, [0]*n
        
        for r,c in indices:
            row_val[r] += 1
            col_val[c] += 1
        
        count = 0
        for i in range(m):
            for j in range(n):
                #Check a cell value is odd or not
                if (row_val[i] + col_val[j]) % 2 == 1:
                    count += 1
        return count