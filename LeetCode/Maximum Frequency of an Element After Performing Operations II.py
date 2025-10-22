from bisect import bisect_left, bisect_right
from typing import Counter, List


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n = len(nums)

        maxi = float('-inf')

        nums.sort()

        freq = Counter(nums)
        s = set()
        for el in nums:
            s.add(el)
            s.add(el - k)
            s.add(el + k)


        for el in s:
            count = bisect_right(nums, el + k) - bisect_left(nums, el - k)
            maxi = max(maxi, freq[el] + min(count - freq[el], numOperations))

        return maxi