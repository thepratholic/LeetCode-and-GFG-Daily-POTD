from collections import defaultdict

class Solution:
    def countSubstr (self, s, k):
        
        n = len(s)
        
        def f(s, k):
            mpp = defaultdict(int)
            
            l, r = 0, 0
            ans = 0
            
            while r < n:
                
                mpp[s[r]] += 1
                
                while len(mpp) > k:
                    mpp[s[l]] -= 1
                    
                    if mpp[s[l]] == 0:
                        del mpp[s[l]]
                        
                    l += 1
                    
                ans += (r - l + 1)
                
                r += 1
                
            return ans
            
        return f(s, k) - f(s, k - 1)