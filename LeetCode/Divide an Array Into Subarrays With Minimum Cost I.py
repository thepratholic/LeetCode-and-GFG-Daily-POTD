from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)

        s = nums[0]

        nums = nums[1:]
        nums.sort()
        return nums[0] + nums[1] + s