from collections import Counter
from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k == 0:
            return len(set(nums))

        nums.sort()
        
        count = 1
        prev = nums[0] - k

        for i in range(1, n):

            cur_mini = max(prev + 1, nums[i] - k)

            if cur_mini <= nums[i] + k:
                count += 1
                prev = cur_mini

            else:
                prev = nums[i] + k

        return count