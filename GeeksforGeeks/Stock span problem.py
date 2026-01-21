class Solution:
    def calculateSpan(self, arr):
        n = len(arr)
        
        stack = []
        ans = []
        
        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
                
            if stack:
                ans.append(i - stack[-1])
                
            else:
                ans.append(i + 1)
                
            stack.append(i)
            
        return ans