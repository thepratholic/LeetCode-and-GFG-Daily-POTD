from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        dp = [1] * m
        lis = 1

        for i in range(1, m):
            for j in range(i):

                valid = True
                for k in range(n):
                    if strs[k][j] > strs[k][i]:
                        valid = False
                        break

                if valid:
                    dp[i] = max(dp[i], dp[j] + 1)

            lis = max(lis, dp[i])

        return m - lis