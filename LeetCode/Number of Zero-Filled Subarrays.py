from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        zeros = [0] * n

        if nums[0] == 0:
            zeros[0] = 1
        for i in range(1, n):
            if nums[i] == 0:
                zeros[i] = 1 + zeros[i - 1]
            else:
                zeros[i] = 0

        ans = 0
        for i in range(n):
            ans += zeros[i]

        return ans