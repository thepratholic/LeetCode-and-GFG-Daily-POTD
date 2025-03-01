from typing import List


class Solution:
    def shiftZeros(self, nums):
        j = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break

        if j == -1: return nums
        for k in range(j + 1, len(nums)):
            if nums[k] != 0:
                nums[j], nums[k] = nums[k], nums[j]
                j += 1

        return nums

    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        # shifting the zeros to the end
        return self.shiftZeros(nums)
