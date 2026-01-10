class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                if s1[i] == s2[j]:
                    dp[i][j] = ord(s1[i]) + dp[i + 1][j + 1]

                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

                

        # def f(i, j):
        #     if i == n or j == m:
        #         return 0

        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     if s1[i] == s2[j]:
        #         dp[i][j] = ord(s1[i]) + f(i + 1, j + 1)

        #     else:
        #         dp[i][j] = max(f(i + 1, j), f(i, j + 1))

        #     return dp[i][j]

        # lcs = f(0, 0)

        total = sum(map(ord, s1)) + sum(map(ord, s2))

        return total - (2 * dp[0][0])