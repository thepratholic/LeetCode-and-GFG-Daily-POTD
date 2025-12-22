from bisect import bisect_right

class Solution:
    def rowWithMax1s(self, arr):
        n = len(arr)
        m = len(arr[0])
        
        ans = -1
        r = -1
        
        for row in range(n):
            idx = bisect_right(arr[row], 0)
            
            if idx == m:
                continue
            else:
                if m - idx > ans:
                    ans = m - idx
                    r = row
                
        return r