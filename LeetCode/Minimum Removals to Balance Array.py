from bisect import bisect_right
from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 1
        nums.sort()

        for i in range(n):
            limit = nums[i] * k

            idx = bisect_right(nums, limit)

            sz = idx - i
            ans = max(ans, sz)

        return n - ans