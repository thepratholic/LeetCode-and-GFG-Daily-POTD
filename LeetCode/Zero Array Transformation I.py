from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)

        for l, r in queries:
            diff[l] -= 1
            if r + 1 < len(diff):
                diff[r + 1] += 1

        for i in range(1, n):
            diff[i] += diff[i - 1]

        for i in range(n):
            if nums[i] + diff[i] > 0:
                return False

        return True
