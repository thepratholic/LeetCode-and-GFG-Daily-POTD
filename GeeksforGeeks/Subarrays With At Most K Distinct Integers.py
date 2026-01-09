from collections import defaultdict

class Solution:
    def countAtMostK(self, arr, k):
        
        n = len(arr)
        mpp = defaultdict(int)
        
        l, r = 0, 0
        
        ans = 0
        
        while r < n:
            
            mpp[arr[r]] += 1
            
            while len(mpp) > k:
                mpp[arr[l]] -= 1
                
                if mpp[arr[l]] == 0:
                    del mpp[arr[l]]
                    
                l += 1
                
            length = (r - l + 1)
            
            ans += length
            
            r += 1
            
        return ans
        