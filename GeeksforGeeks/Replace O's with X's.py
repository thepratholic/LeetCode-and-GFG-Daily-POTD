class Solution:
    def fill(self, grid):
        
        n = len(grid)
        m = len(grid[0])
        
        
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def isValid(i, j):
            return i >= 0 and i < n and j >= 0 and j < m
        
        boundary_cells = set()
        
        def dfs(i, j):
            boundary_cells.add((i, j))
            
            for dx, dy in dirs:
                nRow = dx + i
                nCol = dy + j
                
                if isValid(nRow, nCol):
                    if (nRow, nCol) not in boundary_cells and grid[nRow][nCol] == 'O':
                        dfs(nRow, nCol)
                    
            
        
        for i in range(n):
            
            for j in range(m):
                
                if grid[i][j] == 'O':
                    if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                        dfs(i, j)
                        
                        
            
        
        for i in range(n):
            
            for j in range(m):
                
                if grid[i][j] == 'O' and (i, j) not in boundary_cells:
                    grid[i][j] = 'X'
                    
                    
        return grid