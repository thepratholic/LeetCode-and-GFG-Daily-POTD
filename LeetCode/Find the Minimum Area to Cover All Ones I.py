from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        max_row, min_row = -1, n
        max_col, min_col = -1, m

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_row = max(max_row, i)
                    min_row = min(min_row, i)
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)

        return ((max_row - min_row) + 1) * ((max_col - min_col) + 1)