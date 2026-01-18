from collections import Counter

class Solution:
    def nextFreqGreater(self, arr):
        
        n = len(arr)
        
        freq = Counter(arr)
        ans = [-1] * n
        
        stack = []
        
        for i in range(n - 1, -1, -1):
            while stack and freq[stack[-1]] <= freq[arr[i]]:
                stack.pop()
                
            if stack:
                ans[i] = stack[-1]
                
            stack.append(arr[i])
            
        return ans