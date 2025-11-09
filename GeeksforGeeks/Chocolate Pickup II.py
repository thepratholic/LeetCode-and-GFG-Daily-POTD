class Solution:
    def chocolatePickup(self, mat):
        n = len(mat)
        dp = [[[-1]*n for _ in range(n)] for __ in range(n)]

        def f(r1, c1, r2):
            c2 = r1 + c1 - r2
            if (r1 >= n or c1 >= n or r2 >= n or c2 >= n or 
                mat[r1][c1] == -1 or mat[r2][c2] == -1):
                return float('-inf')

            if r1 == c1 == r2 == c2 == n - 1:
                return mat[n-1][n-1]

            if dp[r1][c1][r2] != -1:
                return dp[r1][c1][r2]

            chocolates = mat[r1][c1]
            if r1 != r2:
                chocolates += mat[r2][c2]

            next_best = max(
                f(r1+1, c1, r2+1),
                f(r1, c1+1, r2),
                f(r1+1, c1, r2),
                f(r1, c1+1, r2+1)
            )

            dp[r1][c1][r2] = chocolates + next_best
            return dp[r1][c1][r2]

        ans = f(0, 0, 0)
        return max(0, ans)
