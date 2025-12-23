from bisect import bisect_left, bisect_right
class Solution:
    def cntInRange(self, arr, queries):
        
        arr.sort()
        
        n = len(arr)
        
        ans = []
        
        for a, b in queries:
            
            f = bisect_left(arr, a)
            s = bisect_right(arr, b)
            
            if f == n:
                ans.append(0)
                
            else:
                ans.append(s - f)
                
        return ans