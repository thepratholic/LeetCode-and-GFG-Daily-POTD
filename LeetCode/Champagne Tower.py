class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        def f(i, j):
            if i < 0 or j < 0 or i < j:
                return 0.0

            if dp[i][j] != -1:
                return dp[i][j]

            if i == 0 and j == 0:
                return poured

            up_left = (f(i - 1, j - 1) - 1) / 2
            up_right = (f(i - 1, j) - 1) / 2

            if up_left < 0:
                up_left = 0.0

            if up_right < 0:
                up_right = 0.0

            dp[i][j] = up_left + up_right
            return dp[i][j]

        dp = [[-1] * (query_glass + 1) for _ in range(query_row + 1)]
        return min(1.0, f(query_row, query_glass))