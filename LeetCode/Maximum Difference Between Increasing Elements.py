from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = float("-inf")
        n = len(nums)
        for i in range(n - 1):
            for j in range(i, n):
                if nums[j] > nums[i]:
                    ans =  max(ans, nums[j] - nums[i])

        return ans if ans != float("-inf") else -1