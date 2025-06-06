from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)

        low, mid, high = 0, 0, n - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                mid += 1
                low += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1