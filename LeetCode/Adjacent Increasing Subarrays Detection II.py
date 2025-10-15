from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        pref = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                pref[i] = pref[i - 1] + 1

        suff = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                suff[i] = suff[i + 1] + 1


        ans = 0
        for i in range(n - 1):
            ans = max(ans, min(pref[i], suff[i + 1]))

        return ans