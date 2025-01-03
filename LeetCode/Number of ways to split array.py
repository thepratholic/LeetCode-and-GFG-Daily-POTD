from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0 
        totalSum = sum(nums)
        left_sum = 0

        for i in range(n-1):
            left_sum += nums[i]
            totalSum -= nums[i]
            if left_sum >= totalSum:
                cnt += 1

        return cnt