from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maximum_sum = float("-inf")

        n = len(nums)

        if n == 1:
            return nums[0]

        for i in range(n):
            current = nums[i]
            for j in range(i+1, n):
                if nums[j] > nums[j-1]:
                    current += nums[j]
                else:
                    break
            maximum_sum = max(maximum_sum, current)

        return maximum_sum