from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        n = len(nums)

        s = set()

        for i in range(n):
            if nums[i] > 0:
                s.add(nums[i])

        if len(s) == 0:
            return max(nums)

        else:
            return sum(s)