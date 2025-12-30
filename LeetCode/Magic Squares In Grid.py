from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0

        def haveSameSum(i, j):
            if grid[i + 1][j + 1] != 5: return False
            seen = set()
            for r in range(i, i + 3):
                for c in range(j, j + 3):
                    val = grid[r][c]
                    if val < 1 or val > 9 or val in seen: return False
                    seen.add(val)

            for r in range(3):
                if sum(grid[i + r][j:j + 3]) != 15:
                    return False

            for c in range(3):
                if grid[i][j + c] + grid[i + 1][j + c] + grid[i + 2][j + c] != 15:
                    return False

            if grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] != 15:
                return False

            if grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] != 15:
                return False

            return True

        for i in range(n - 2):
            for j in range(m - 2):
                if haveSameSum(i, j):
                    ans += 1

        return ans