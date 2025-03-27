from collections import defaultdict
from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)

        first = defaultdict(int)
        second = defaultdict(int)

        for i in nums:
            second[i] += 1

        for i in range(n):
            second[nums[i]] -= 1
            first[nums[i]] += 1

            if first[nums[i]] * 2 > i+1 and second[nums[i]] * 2 > n - i - 1:
                return i

        return -1