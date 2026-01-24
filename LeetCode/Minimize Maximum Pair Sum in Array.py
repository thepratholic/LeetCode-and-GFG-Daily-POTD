from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        def check(t):
            for i in range(n // 2):
                if nums[i] + nums[n - i - 1] > t:
                    return False

            return True

        ans = nums[-1] + nums[-2]
        low, high = nums[0] + nums[1], nums[-1] + nums[-2]

        while low <= high:
            mid = (low + high) >> 1

            if check(mid):
                ans = mid
                high = mid - 1

            else:
                low = mid + 1

        return ans