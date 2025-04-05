from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)

        OR = 0
        for num in nums:
            OR |= num

        return OR * (1 << (len(nums) - 1))