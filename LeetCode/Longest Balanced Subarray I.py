from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0
        for i in range(n):
            odd, even = set(), set()

            for j in range(i, n):
                if nums[j] & 1:
                    odd.add(nums[j])
                else:
                    even.add(nums[j])


                if len(odd) == len(even):
                    ans = max(ans, j - i + 1)

        return ans