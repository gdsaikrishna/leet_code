class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        mid, res = n // 2, 0
        
        for i in range(n):
            res += mat[i][i]
            res += mat[n-1-i][i]
            
        if n % 2 == 1:
            res -= mat[mid][mid]
            
        return res