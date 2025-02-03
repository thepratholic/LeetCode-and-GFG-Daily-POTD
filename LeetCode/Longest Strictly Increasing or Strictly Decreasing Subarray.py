from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxi = 0

        for i in range(len(nums)):
            curr = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[j-1]:
                    curr += 1
                else:
                    break

            maxi = max(maxi, curr)

        for i in range(len(nums)):
            curr = 1
            for j in range(i+1, len(nums)):
                if nums[j] < nums[j-1]:
                    curr += 1
                else:
                    break

            maxi = max(maxi, curr)

        return maxi