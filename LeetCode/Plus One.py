from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        ans = 0

        for x in digits:
            ans = (ans * 10) + x

        ans += 1

        l = []

        while ans > 0:
            ld = ans % 10
            ans //= 10
            l.append(ld)

        return l[::-1]