from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        cnt = 0

        for i in range(2, n):
            if nums[i - 2] == 0:
                cnt += 1

                nums[i - 2] ^= 1
                nums[i - 1] ^= 1
                nums[i] ^= 1

        if sum(nums) != len(nums):
            return cnt

        return -1