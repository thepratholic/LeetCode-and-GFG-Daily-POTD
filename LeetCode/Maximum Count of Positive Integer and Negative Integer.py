from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        pos, neg = 0, 0

        for i in range(n):
            if nums[i] == 0:
                continue

            if nums[i] < 0:
                neg += 1
            else:
                pos += 1

        return max(pos, neg)