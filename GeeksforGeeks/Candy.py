class Solution:
    def minCandy(self, arr):
        n = len(arr)
        
        ans = 0
        left = [0] * n
        right = [0] * n
        
        left[0] = 1
        right[-1] = 1
        
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                left[i] += (left[i - 1] + 1)
                
            else:
                left[i] = 1
                
        
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                right[i] = right[i + 1] + 1
                
            else:
                right[i] = 1
                
        
        for i in range(n):
            ans += max(left[i], right[i])
            
        return ans