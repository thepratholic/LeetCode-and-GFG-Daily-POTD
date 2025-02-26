from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maximum_sum = float('-inf')
        n = len(nums)

        current = 0
        for i in range(n):
            current += nums[i]
            maximum_sum = max(maximum_sum, current)
            if current < 0:
                current = 0

        minimum_sum = float('inf')
        current = 0
        for i in range(n):
            current += nums[i]
            minimum_sum = min(minimum_sum, current)
            if current > 0:
                current = 0

        return max(maximum_sum, abs(minimum_sum))