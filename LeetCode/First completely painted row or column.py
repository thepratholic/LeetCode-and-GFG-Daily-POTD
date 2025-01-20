from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        pos_map = {}
        for i in range(m):
            for j in range(n):
                pos_map[mat[i][j]] = (i, j)
        rowCount = [0] * m
        colCount = [0] * n

        total_cells = n*m

        for i in range(total_cells):
            cell = pos_map[arr[i]]

            rowCount[cell[0]] += 1
            colCount[cell[1]] += 1

            if rowCount[cell[0]] == n and colCount[cell[1]] == m:
                return i

        return -1
