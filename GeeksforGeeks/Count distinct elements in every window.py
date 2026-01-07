from collections import defaultdict

class Solution:
    def countDistinct(self, arr, k):
        
        n = len(arr)
        
        l, r = 0, k
        
        ans = []
        
        mpp = defaultdict(int)
        
        for i in range(k):
            mpp[arr[i]] += 1
            
        ans.append(len(mpp))
        
        while r < n:
            
            mpp[arr[r]] += 1
            
            mpp[arr[l]] -= 1
            if mpp[arr[l]] == 0:
                del mpp[arr[l]]
                
            ans.append(len(mpp))
            
            r += 1
            l += 1
            
        return ans