from typing import Counter, List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)

        maxi = max(freq.values())
        ans = 0

        for k, v in freq.items():
            if v == maxi:
                ans += v

        return ans