from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        result = []

        visP = [[False] * n for _ in range(m)]
        visA = [[False] * n for _ in range(m)]

        pq, aq = deque(), deque()

        # for pacific ocean
        for i in range(m):
            pq.append((i, 0))
            visP[i][0] = True

        for j in range(n):
            pq.append((0, j))
            visP[0][j] = True

        # for atlantic ocean
        for i in range(m):
            aq.append((i, n - 1))
            visA[i][n - 1] = True

        for j in range(n):
            aq.append((m - 1, j))
            visA[m - 1][j] = True

        def isValid(i, j):
            return i >= 0 and i < m and j >= 0 and j < n


        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def bfs(q, vis):
            while q:
                i, j = q.popleft()

                for dx, dy in dirs:
                    nRow, nCol = i + dx, j + dy

                    if isValid(nRow, nCol) and not vis[nRow][nCol] and heights[nRow][nCol] >= heights[i][j]:
                        vis[nRow][nCol] = True
                        q.append((nRow, nCol))


        bfs(pq, visP)
        bfs(aq, visA)

        for i in range(m):
            for j in range(n):

                if visP[i][j] and visA[i][j]:
                    result.append((i, j))


        return result