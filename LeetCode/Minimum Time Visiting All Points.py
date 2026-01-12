from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        for i in range(n - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]

            dx = abs(x2 - x1)
            dy = abs(y2 - y1)

            ans += max(dx, dy)

        return ans