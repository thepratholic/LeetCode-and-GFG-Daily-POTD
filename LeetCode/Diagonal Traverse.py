from collections import deque
from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])

        q = deque()
        vis = set()

        q.append((0, 0)) # row, col
        vis.add((0, 0)) # marking the cell as visited
        level = 0

        ans = []

        while q:
            length = len(q)
            cur = []

            for _ in range(length):

                i, j = q.popleft()
                cur.append(mat[i][j])

                if j + 1 < m and (i, j + 1) not in vis:
                    vis.add((i, j + 1))
                    q.append((i, j + 1))

                if i + 1 < n and (i + 1, j) not in vis:
                    vis.add((i + 1, j))
                    q.append((i + 1, j))

                
            if level & 1:
                ans.extend(cur)
            else:
                cur = cur[::-1]
                ans.extend(cur)

            level += 1

        return ans