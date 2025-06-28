from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        
        values = []

        for index, element in enumerate(nums):
            values.append((index, element))

        values.sort(key = lambda x : x[1], reverse = True)

        values = sorted(values[:k])

        return [v for i, v in values]