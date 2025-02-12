from collections import defaultdict
from typing import List

class Solution:
    def sumOfNumDigits(self, num):
        ans = 0
        while num > 0:
            ld = num % 10
            ans += (ld)
            num //= 10
        return ans

    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)

        mpp = defaultdict(list)

        for i in range(n):
            ans = self.sumOfNumDigits(nums[i])
            mpp[ans].append(nums[i])

        maxi = -1
        
        for k, v in mpp.items():
            if len(v) >= 2:
                v.sort(reverse=True)

                ans = v[0] + v[1]
                maxi = max(maxi, ans)

        return maxi