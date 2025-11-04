class Solution:
    def minCost(self, height):
        
        n = len(height)
        
        def f(idx):
            if idx >= n - 1:
                return 0
                
            if dp[idx] != -1:
                return dp[idx]
                
            one = abs(height[idx] - height[idx + 1]) + f(idx + 1)
            
            two = float('inf')
            if idx + 2 < n:
                two = abs(height[idx] - height[idx + 2]) + f(idx + 2)
                
            dp[idx] = min(one, two)
            return dp[idx]
            
        dp = [-1] * n
        return f(0)