from math import gcd
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        cnt1 = nums.count(1)
        if cnt1 > 0:
            return n - cnt1

        
        ans = float('inf')
        for i in range(n - 1):
            gcd_ = nums[i]

            for j in range(i + 1, n):
                gcd_ = gcd(gcd_, nums[j])
                if gcd_ == 1:
                    ans = min(ans, (j - i) + (n - 1))
                    break

        return ans if ans != float('inf') else -1