from typing import List


class Solution:

    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        total = 0

        for i in range(m):
            row_ones_count = grid[i].count(1)
            for j in range(n):
                col_ones_count = sum(grid[row][j] for row in range(m))
                if grid[i][j] and (col_ones_count > 1 or row_ones_count > 1):
                    total += 1
        return total


