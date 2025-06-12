from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float("-inf")

        for i in range(n - 1):
            ans = max(ans, abs(nums[i] - nums[i + 1]))

        ans = max(ans, abs(nums[0] - nums[-1]))

        return ans