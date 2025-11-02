from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        unique_guards = {tuple(g) for g in guards}
        unique_walls = {tuple(w) for w in walls}

        guarded = set()

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def isValid(i, j):
            return i >= 0 and i < m and j >= 0 and j < n

        for r, c in unique_guards:
            for x, y in dirs:
                nRow, nCol = r + x, c + y

                while isValid(nRow, nCol) and (nRow, nCol) not in unique_walls and (nRow, nCol) not in unique_guards:
                    guarded.add((nRow, nCol))
                    nRow += x
                    nCol += y

        empty = (m * n) - len(guards) - len(walls)
        return empty - len(guarded)