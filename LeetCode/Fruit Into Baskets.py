from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        n = len(nums)

        ans = float('-inf')
        mpp = defaultdict(int)

        l, r = 0, 0

        while r < n:
            mpp[nums[r]] += 1

            if len(mpp) > 2:
                while mpp[nums[l]] > 0:
                    mpp[nums[l]] -= 1
                    if mpp[nums[l]] == 0:
                        del mpp[nums[l]]
                        break
                    l += 1
                l += 1

            ans = max(ans, r - l + 1)
            r += 1
        return ans