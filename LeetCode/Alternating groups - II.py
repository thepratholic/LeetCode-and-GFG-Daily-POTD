from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[:k - 1])

        n = len(colors)

        cnt = 0
        l, r = 0, 1

        while r < n:
            if colors[r] == colors[r - 1]:
                l = r
                r += 1
                continue

            if r - l + 1 == k:
                cnt += 1
                l += 1
            r += 1

        return cnt