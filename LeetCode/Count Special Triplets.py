from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = (10 ** 9) + 7
        n = len(nums)
        mpp = defaultdict(list)

        for i, v in enumerate(nums):
            mpp[v].append(i)

        ans = 0
        for j in range(n):

            target = nums[j] * 2

            if target not in mpp: continue

            v = mpp[target]

            i_count = bisect_left(v, j)

            k_count = len(v) - bisect_right(v, j)

            ans = (ans + (i_count * k_count)) % MOD

        return ans