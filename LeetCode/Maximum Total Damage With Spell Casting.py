from bisect import bisect_right
from typing import Counter, List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        n = len(power)
        freq = Counter(power)
        if n == 1:
            return power[0]

        power.sort()

        def f(idx):
            if idx >= n:
                return 0

            if dp[idx] != -1:
                return dp[idx]

            notTake = f(idx + 1)
            nxt = power[idx] + 2
            next_idx = bisect_right(power, nxt)
            take = power[idx] * freq[power[idx]] + f(next_idx)

            dp[idx] = max(take, notTake)
            return dp[idx]

        dp = [-1] * n
        return f(0)