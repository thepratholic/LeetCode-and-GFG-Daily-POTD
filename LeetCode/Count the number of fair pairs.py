from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        left, right = 0, n - 1
        cnt_within_upper = 0

        while left < right:
            if nums[left] + nums[right] <= upper:
                cnt_within_upper += (right - left)
                left += 1

            else:
                right -= 1

        
        left, right = 0, n - 1
        cnt_below_lower = 0

        while left < right:
            if nums[left] + nums[right] < lower:
                cnt_below_lower += (right - left)
                left += 1
            else:
                right -= 1

        return cnt_within_upper - cnt_below_lower