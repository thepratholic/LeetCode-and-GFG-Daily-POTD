from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, 0
        sum, size = 0, 0

        cnt = 0

        while r < n:
            sum += nums[r]
            size += 1

            while l <= r and sum * size >= k:
                sum -= nums[l]
                size -= 1
                l += 1

            cnt += (r - l + 1)
            r += 1

        return cnt