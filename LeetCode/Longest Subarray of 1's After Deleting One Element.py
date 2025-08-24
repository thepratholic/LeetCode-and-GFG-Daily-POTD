from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        f = False
        zeros = 0

        l, r = 0, 0
        ans = float('-inf')
        while r < n:

            if nums[r] == 0:
                zeros += 1
                f = True

            while zeros > 1 and l <= r:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            if f:
                ans = max(ans, (r - l + 1) - zeros)

            else:
                ans = max(ans, (r - l + 1) - 1)

            r += 1

        return ans