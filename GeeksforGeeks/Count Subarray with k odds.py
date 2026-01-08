class Solution:
    def countSubarrays(self, arr, k):
        
        def f(arr, k):
            n = len(arr)
            
            l = 0
            ans = 0
            odd = 0
            
            for r in range(n):
                
                if arr[r] & 1:
                    odd += 1
                    
                while odd > k:
                    if arr[l] & 1:
                        odd -= 1
                    l += 1
                    
                ans += (r - l + 1)
            
        
            return ans
            
        return f(arr, k) - f(arr, k - 1)