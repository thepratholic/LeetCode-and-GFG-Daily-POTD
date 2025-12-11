from bisect import bisect_left
from collections import defaultdict
from typing import List
from sortedcontainers import SortedList


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        
        rows = defaultdict(SortedList)
        cols = defaultdict(SortedList)

        for x, y in buildings:
            rows[x].add(y)
            cols[y].add(x)


        ans = 0
        for x, y in buildings:
            if x == 1 or x == n or y == 1 or y == n:
                continue

            yi = bisect_left(rows[x], y)
            if yi == 0 or yi == len(rows[x]) - 1:
                continue

            xi = bisect_left(cols[y], x)
            if xi == 0 or xi == len(cols[y]) - 1:
                continue

            ans += 1

        return ans