import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])

        def isValid(i, j):
            return i >= 0 and i < m and j >= 0 and j < n

        pq = []

        vis = [[False] * n for _ in range(m)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # insert all the boundary cell values to the min-heap
        for i in range(m):
            if i == 0 or i == m - 1:

                for j in range(n):
                    heapq.heappush(pq, (heightMap[i][j], (i, j)))
                    vis[i][j] = True

            else:
                heapq.heappush(pq, (heightMap[i][0], (i, 0)))
                heapq.heappush(pq, (heightMap[i][n - 1], (i, n - 1)))
                vis[i][0] = True
                vis[i][n - 1] = True


        water = 0
        while pq:
            height, (i, j) = heapq.heappop(pq)

            for dx, dy in dirs:
                nRow = dx + i
                nCol = dy + j

                if isValid(nRow, nCol) and not vis[nRow][nCol]:
                    nHeight = heightMap[nRow][nCol]
                    water += max(0, height - nHeight)

                    heapq.heappush(pq, (max(height, nHeight), (nRow, nCol)))

                    vis[nRow][nCol] = True

        return water