class Solution:
    def numberOfPath(self, mat, k):
        
        n = len(mat)
        m = len(mat[0])
        
        
        def f(i, j, sum_):
            if i >= n or j >= m:
                return 0
                
            sum_ += mat[i][j]
            
            if sum_ > k: return 0
                
            if i == n - 1 and j == m - 1:
                return 1 if sum_ == k else 0
                
            if dp[i][j][sum_] != -1:
                return dp[i][j][sum_]
                
            
            right = f(i, j + 1, sum_)
            
            down = f(i + 1, j, sum_)
            
            dp[i][j][sum_] = down + right
            return dp[i][j][sum_]
            
        dp = [[[-1] * (k + 1) for _ in range(m)] for _ in range(n)]
        return f(0, 0, 0)

