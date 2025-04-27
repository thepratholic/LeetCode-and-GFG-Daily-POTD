from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(n - 2):
            if 2 * (nums[i] + nums[i + 2]) == nums[i + 1]:
                ans += 1

        return ans