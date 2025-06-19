from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        ans = 1

        mini = nums[0]

        for i in nums:
            if i - mini > k:
                ans += 1
                mini = i

        return ans