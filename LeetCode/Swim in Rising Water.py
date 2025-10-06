import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        vis = [[False] * n for _ in range(n)]
        pq = []

        dirs = [(0, 1), (-1, 0), (1, 0), (0, -1)]

        def isValid(i, j):
            return i >= 0 and i < n and j >= 0 and j < n

        t = grid[0][0]

        heapq.heappush(pq, (t, (0, 0)))
        vis[0][0] = True

        while pq:
            cur_t, (i, j) = heapq.heappop(pq)

            if i == n - 1 and j == n - 1:
                return cur_t

            for dx, dy in dirs:
                nRow, nCol = i + dx, j + dy

                if isValid(nRow, nCol) and not vis[nRow][nCol]:
                    nxt = grid[nRow][nCol]
                    heapq.heappush(pq, (max(nxt, cur_t), (nRow, nCol)))
                    vis[nRow][nCol] = True

        return -1