from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        total = sum(nums)
        pref = 0

        for i in range(n - 1):
            pref += nums[i]

            if abs(pref - (total - pref)) % 2 == 0:
                ans += 1

        return ans