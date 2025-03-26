from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        for row in grid:
            for e in row:
                if e % x != grid[0][0] % x:
                    return -1

        nums = sorted([ele for row in grid for ele in row])

        prefix = 0
        total = sum(nums)
        ans = float("inf")

        for i in range(len(nums)):
            cost_left = nums[i] * i - prefix
            cost_right = total - prefix - (nums[i] * (len(nums) - i))
            ops = (cost_left + cost_right) // x
            ans = min(ans, ops)
            prefix += nums[i]

        return ans