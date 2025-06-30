from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n = len(nums)

        nums.sort()

        ans = 0

        l, r = 0, 1

        while r < n:
            if nums[r] - nums[l] == 1:
                ans = max(ans, r - l + 1)

            while nums[r] - nums[l] > 1:
                    l += 1

            r += 1

        return ans