from typing import List


class Solution:
    def f(self, nums, k, mid):
        cnt = 0
        i = 0
        while i < len(nums):
            if nums[i] <= mid:
                cnt += 1
                i += 2
            else:
                i += 1
        return cnt >= k

    def minCapability(self, nums: List[int], k: int) -> int:
        ans = -1
        low, high = 0, max(nums)

        while low <= high:
            mid = (low + high) >> 1

            if self.f(nums, k, mid):
                ans = mid 
                high = mid - 1

            else:
                low = mid + 1

        return ans