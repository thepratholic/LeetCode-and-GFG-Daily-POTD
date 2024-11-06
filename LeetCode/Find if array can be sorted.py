from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def count_bits(n):
            return bin(n).count("1")

        curMin, curMax = nums[0], nums[0]

        prevMax = float("-inf")
        for n in nums:
            if count_bits(n) == count_bits(curMin):
                curMin = min(curMin, n)
                curMax = max(curMax, n)
            else:
                if curMin < prevMax:
                    return False
                prevMax = curMax
                curMin, curMax = n, n + 1
        if curMin < prevMax:
            return False
        return True