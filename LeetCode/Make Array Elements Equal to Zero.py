from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)

        total_sum = sum(nums)
        left_sum = 0
        ans = 0

        for i in range(n):
            left_sum += nums[i]
            right_sum = total_sum - left_sum

            if nums[i] == 0:

                if left_sum == right_sum:
                    ans += 2

                elif abs(left_sum - right_sum) == 1:
                    ans += 1

        return ans