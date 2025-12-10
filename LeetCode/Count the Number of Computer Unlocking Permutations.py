from typing import List


class Solution:
    def countPermutations(self, c: List[int]) -> int:
        n = len(c)
        MOD = (10 ** 9) + 7

        if min(c) != c[0]: return 0

        if c.count(c[0]) != 1: return 0

        ans = 1
        for i in range(1, n):
            ans *= i
            ans %= MOD

        return ans