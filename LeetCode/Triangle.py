from typing import List


class Solution:
    def minimumTotal(self, tri: List[List[int]]) -> int:
        n = len(tri)

        dp = [[0] * (n) for _ in range(n)]

        for i in range(n):
            dp[n - 1][i] = tri[n - 1][i]

        for cur_row in range(n - 2, -1, -1):
            for i in range(cur_row, -1, -1):

                first = dp[cur_row + 1][i] + tri[cur_row][i]
                second = dp[cur_row + 1][i + 1] + tri[cur_row][i]

                dp[cur_row][i] = min(first, second)

        return dp[0][0]