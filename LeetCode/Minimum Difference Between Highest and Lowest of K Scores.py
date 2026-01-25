from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = float('inf')
        
        if k == 1:
            return 0

        l, r = 0, 0

        while r < n:

            if r - l + 1 == k:
                ans = min(ans, nums[r] - nums[l])
                l += 1

            r += 1

        return ans