from math import inf
from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)

        # res = [inf]

        def f(i, j):
            if j - i + 1 < 3:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            ans = inf
            for k in range(i + 1, j):
                t = values[i] * values[j] * values[k]
                wt = f(i, k) + t + f(k, j)

                ans = min(ans, wt)

            dp[i][j] = ans
            return dp[i][j]

        dp = [[-1] * n for _ in range(n)]
        return f(0, n - 1)