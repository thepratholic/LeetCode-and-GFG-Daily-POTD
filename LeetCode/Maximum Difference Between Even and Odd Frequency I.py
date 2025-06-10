from collections import defaultdict


class Solution:
    def maxDifference(self, s: str) -> int:
        n = len(s)

        mpp = defaultdict(int)

        for i in s:
            mpp[i] += 1

        max_even, max_odd = float('inf'), 0

        for v in mpp.values():
            if v % 2 == 1:
                max_odd = max(max_odd, v)
            else:
                max_even = min(max_even, v)

        return max_odd - max_even