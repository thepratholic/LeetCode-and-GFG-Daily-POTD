from bisect import bisect_left, bisect_right

class Solution:
    def countXInRange(self, arr, queries):
        n = len(queries)
        
        ans = []
        
        
        for l, r, x in queries:
            
            f = bisect_left(arr, x, l, r + 1)
            s = bisect_right(arr, x, l, r + 1)
            
            if f == r + 1:
                ans.append(0)
                
                continue
            
            else:
                ans.append(s - f)
                
        return ans