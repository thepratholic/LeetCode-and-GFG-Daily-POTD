class Solution:
    def maxPeople(self, arr):
        n = len(arr)
        pge = [-1] * n
        nge = [n] * n
        stack = []
        
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
                
            pge[i] = stack[-1] if stack else -1
            stack.append(i)
            
        stack.clear()
        
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
                
            nge[i] = stack[-1] if stack else n
            
            stack.append(i)
            
        ans = 0
        
        for i in range(n):
            left = i - pge[i] - 1
            right = nge[i] - i - 1
            ans = max(ans, left + right + 1)
            
        return ans