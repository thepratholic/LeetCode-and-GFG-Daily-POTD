from typing import List


class Solution:
    def f(self, mid, nums, p):
        cnt = 0
        n = len(nums)
        i = 0
        while i < n - 1:
            if(nums[i + 1] - nums[i] <= mid):
                cnt += 1
                i += 2
            else:
                i += 1
    
        return cnt >= p

    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        low, high = 0, nums[-1] - nums[0]
        ans = float("inf")

        while low <= high:
            mid = (low + high) >> 1

            if self.f(mid, nums, p):
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1

        return ans