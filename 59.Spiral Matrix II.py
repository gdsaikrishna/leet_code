class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A = [[0] * n for _ in range(n)]
        i, j, i_add, j_add = 0, 0, 0, 1
        for k in range(n*n):
            A[i][j] = k + 1
            if A[(i+i_add)%n][(j+j_add)%n]:
                i_add, j_add = j_add, -i_add
            i += i_add
            j += j_add
        return A