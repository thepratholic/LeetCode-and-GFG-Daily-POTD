from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)

        res, i_maxi, d_maxi = 0, 0, 0

        for k in range(n):
            res = max(res, nums[k] * d_maxi)
            d_maxi = max(d_maxi, i_maxi - nums[k])
            i_maxi = max(i_maxi, nums[k])

        return res