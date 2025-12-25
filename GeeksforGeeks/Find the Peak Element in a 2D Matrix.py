class Solution:
    def findPeakGrid(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        def isValid(i, j):
            return 0 <= i < n and 0 <= j < m
        
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        for i in range(n):
            for j in range(m):
                
                isPeak = True
                
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    
                    if 0 <= ni < n and 0 <= nj < m:
                        if mat[ni][nj] > mat[i][j]:
                            isPeak = False
                            break
                
                if isPeak:
                    return [i, j]