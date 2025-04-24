from collections import defaultdict
from typing import List
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        mpp = defaultdict(int)
        total = len(set(nums))
        inside = 0

        ans, l, r = 0, 0, 0

        while l < n:
            while r < n and inside < total:
                if mpp[nums[r]] == 0:
                    inside += 1
                mpp[nums[r]] += 1
                r += 1

            if inside == total:
                ans += (n - r + 1)

            mpp[nums[l]] -= 1
            if mpp[nums[l]] == 0:
                inside -= 1

            l += 10

        return ans