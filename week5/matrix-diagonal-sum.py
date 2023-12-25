class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        sum_diagonal =0
        n = len(mat)
        for i in range(n):
            sum_diagonal += mat[i][i] + mat[i][n-1-i]
        if n%2:
            sum_diagonal -= mat[n//2][n//2]
        return sum_diagonal