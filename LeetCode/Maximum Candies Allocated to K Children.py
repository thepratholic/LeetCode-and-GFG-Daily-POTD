from typing import List


class Solution:
    def f(self, candies, k, mid):
        cnt = 0
        for i in candies:
            cnt += (i // mid)
        return cnt >= k

    def maximumCandies(self, candies: List[int], k: int) -> int:
        n = len(candies)
        low, high, ans = 1, max(candies), 0

        while low <= high:
            mid = (low + high) >> 1

            if self.f(candies, k, mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
        