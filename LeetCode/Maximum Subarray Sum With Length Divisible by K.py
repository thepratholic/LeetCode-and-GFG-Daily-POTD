from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        pref = [0] * n
        pref[0] = nums[0]

        for i in range(1, n):
            pref[i] = pref[i - 1] + nums[i]

        ans = float('-inf')
        cur_sum = 0
        for start in range(k):
            i = start
            cur_sum = 0

            while i < n and i + k - 1 < n:
                j = i + k - 1
                sub_sum = pref[j] - (pref[i - 1] if i > 0 else 0)
                cur_sum = max(sub_sum, cur_sum + sub_sum)
                ans = max(ans, cur_sum)

                i += k

        return ans