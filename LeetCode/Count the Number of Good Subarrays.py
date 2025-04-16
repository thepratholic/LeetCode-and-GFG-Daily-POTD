from collections import defaultdict
from typing import List
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        l, r, ans, res, pairs = 0, 0, 0, 0, 0
        freq = defaultdict(int)

        for r in range(len(nums)):
            pairs += freq[nums[r]]
            freq[nums[r]] += 1

            while pairs >= k:
                res += len(nums) - r
                freq[nums[l]] -= 1
                pairs -= freq[nums[l]]
                l += 1

        return res