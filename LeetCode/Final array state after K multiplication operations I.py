from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            mini = min(nums)
            min_index = nums.index(mini)
            nums[min_index] *= multiplier
        return nums