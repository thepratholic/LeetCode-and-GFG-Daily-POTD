class Solution:
    def productExceptSelf(self, arr):
        #code here
        n = len(arr)
        if n == 1:
            return []
            
        pre, suff, res = [1] * n, [1] * n, [1] * n
        
        pre[0] = arr[0]
        
        for i in range(1, n):
            pre[i] = arr[i] * pre[i-1]
            
        suff[n-1] = arr[n-1]
        
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * arr[i]
        
        res[0] = suff[1]
        res[n-1] = pre[n-2]
        for i in range(1, n-1):
            res[i] = pre[i-1] * suff[i+1]
            
        return res