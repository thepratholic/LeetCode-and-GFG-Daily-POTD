from collections import defaultdict
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = (10 ** 9) + 7
        ans = 0
        
        y_points = defaultdict(int)
        for x, y in points:
            y_points[y] += 1

        total = 0

        for y, count in y_points.items():
            
            hori_lines = count * (count - 1) // 2
            ans = (ans + (hori_lines * total)) % MOD
            total += hori_lines

        return ans % MOD