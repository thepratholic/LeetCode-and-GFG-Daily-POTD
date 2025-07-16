from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)

        odds, evens = 0, 0

        # counting for even and odd subsequences as they both are valid
        for i in nums:
            if i & 1:
                odds += 1
            else:
                evens += 1

        # now we will be counting for alternating parity subsequences
        alt = 1
        prev = nums[0] % 2

        for i in range(1, n):
            cur = nums[i] % 2

            if cur != prev:
                alt += 1
                prev = cur

        return max(evens, odds, alt)