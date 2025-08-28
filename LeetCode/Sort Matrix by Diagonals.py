from typing import List


class Solution:
    def f(self, i, j, asc, grid):
        n = len(grid)
        diagonal = []
        row, col = i, j

        while row < n and col < n:
            diagonal.append(grid[row][col])
            row += 1
            col += 1

        if asc:
            diagonal.sort()

        else:
            diagonal.sort(reverse = True)

        row, col = i, j
        ptr = 0
        while row < n and col < n:
            grid[row][col] = diagonal[ptr]
            row += 1
            col += 1
            ptr += 1



    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        
        
        for j in range(1, n):
            self.f(0, j, True, grid)

        
        for i in range(n):
            self.f(i, 0, False, grid)

        return grid