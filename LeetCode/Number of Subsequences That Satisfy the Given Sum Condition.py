from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        M = 10 ** 9 + 7 
        nums.sort()
        n = len(nums)
        power = [-1] * n
        power[0] = 1
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % M

        
        l, r = 0, n - 1
        ans = 0
        while l <= r:
            if nums[l] + nums[r] <= target:
                ans += power[r - l] % M
                l += 1

            else:
                r -= 1

        return ans % M