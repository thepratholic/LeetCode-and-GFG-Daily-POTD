from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)

        p = 0
        while p + 1 < n and nums[p] < nums[p + 1]:
            p += 1

        if p == 0:
            return False

        while p + 1 < n and nums[p] > nums[p + 1]:
            p += 1

        if p == n - 1:
            return False

        while p + 1 < n and nums[p] < nums[p + 1]:
            p += 1

        return p == n - 1