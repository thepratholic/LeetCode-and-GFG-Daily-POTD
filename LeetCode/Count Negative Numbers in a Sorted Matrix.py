import bisect
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for row in grid:
            row.sort()

        negs = 0

        for row in grid:
            idx = bisect.bisect_left(row, 0)
            
            negs += (idx - 0)

        return negs