from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        xi = 0
        ans = []
        for b in nums:
            xi = (xi * 2 + b) % 5
            ans.append(xi == 0)
        return ans