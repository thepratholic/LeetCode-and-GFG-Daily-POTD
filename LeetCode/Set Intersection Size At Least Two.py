from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        
        intervals.sort(key = lambda x : (x[1], -x[0]))

        ans = 0
        f, s = -1, -1

        for l, r in intervals:

            if l <= f:
                continue

            if l <= s:
                f = s
                s = r
                ans += 1

            else:
                ans += 2
                s = r
                f = r - 1

        return ans
        