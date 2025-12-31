from collections import deque
from typing import List


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        def isValid(i, j):
            return 0 <= i < row and 0 <= j < col
        
        def check(day):
            grid = [[0] * col for _ in range(row)]

            for i in range(day):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1

            q = deque()
            vis = [[False] * col for _ in range(row)]
            for c in range(col):
                if grid[0][c] == 0:
                    q.append((0, c))
                    vis[0][c] = True

            dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

            while q:
                r, c = q.popleft()

                if r == row - 1:
                    return True

                for dx, dy in dirs:
                    nRow, nCol = r + dx, c + dy

                    if isValid(nRow, nCol) and grid[nRow][nCol] == 0 and not vis[nRow][nCol]:
                        q.append((nRow, nCol))
                        vis[nRow][nCol] = True

            return False

        
        low, high = 0, len(cells)
        ans = 0

        while low <= high:
            mid = (low + high) >> 1

            if check(mid):
                ans = mid
                low = mid + 1

            else:
                high = mid - 1

        return ans