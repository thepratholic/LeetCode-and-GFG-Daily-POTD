from functools import lru_cache
from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def f(i, rem):
            if i >= n:
                return 0 if rem == 0 else float('-inf')

            not_take = f(i + 1, rem)
            take = nums[i] + f(i + 1, (rem + nums[i]) % 3)

            return max(not_take, take)

        return f(0, 0)