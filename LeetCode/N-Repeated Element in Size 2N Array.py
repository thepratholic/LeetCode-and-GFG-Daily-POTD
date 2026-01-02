from typing import Counter, List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        t = len(nums) // 2

        freq = Counter(nums)

        for k, v in freq.items():
            if v == t:
                return k