class Solution:
    def maxSubarrayXOR(self, arr, k):
        # code here
        
        n = len(arr)
        
        prefXor = [0] * n
        
        prefXor[0] = arr[0]
        
        for i in range(1, n):
            prefXor[i] = prefXor[i - 1] ^ arr[i]
            
        ans = float('-inf')
        
        l, r = 0, k - 1
        
        while r < n:
            
            if l > 0:
                ans = max(ans, prefXor[r] ^ prefXor[l - 1])
                
            else:
                ans = max(ans, prefXor[r])
                
            l += 1
            r += 1
            
        return ans