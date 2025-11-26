from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = (10 ** 9) + 7

        # @lru_cache(None)
        def f(i, j, cur_sum):
            if i >= m or j >= n:
                return 0

            if i == m - 1 and j == n - 1:
                cur_sum += grid[i][j]
                return 1 if cur_sum % k == 0 else 0

            if dp[i][j][cur_sum] != -1:
                return dp[i][j][cur_sum]

            right = f(i, j + 1, (cur_sum + grid[i][j]) % k)
            down = f(i + 1, j, (cur_sum + grid[i][j]) % k)

            dp[i][j][cur_sum] = (right + down) % MOD
            return dp[i][j][cur_sum]

        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
        return f(0, 0, 0)