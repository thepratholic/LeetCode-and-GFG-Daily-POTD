class Solution:
	def minSquares(self, n):
		# Code here
		
		
# 		def f(target):
		    
# 		    if target == 0:
# 		        return 0
		        
# 		    if dp[target] != -1:
# 		        return dp[target]
		        
		    
# 		    start = 1
# 		    ans = float('inf')
		    
# 		    while start * start <= target:
# 		        ans = min(ans, 1 + f(target - (start * start)))
# 		        start += 1
		        
# 		    dp[target] = ans
# 		    return dp[target]
		    
		dp = [0] * (n + 1)
		dp[0] = 0
		
		for target in range(1, n + 1):
		    
		    start = 1
		    ans = float('inf')
		    
		    while start * start <= target:
		        ans = min(ans, 1 + dp[target - (start * start)])
		        start += 1
		        
		    dp[target] = ans
		return dp[n]
	
