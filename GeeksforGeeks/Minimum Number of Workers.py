class Solution:
    def minMen(self, arr):
        n = len(arr)

        intervals = []
    
        for i in range(n):
            if arr[i] != -1:
                L = max(0, i - arr[i])
                R = min(n - 1, i + arr[i])
                intervals.append((L, R))
    
        intervals.sort()
        
        if not intervals or intervals[0][0] > 0:
            return -1
    
        cnt = 0
        i = 0
        curr_end = 0
        max_end = 0
    
        while curr_end <= n - 1:
            
            while i < len(intervals) and intervals[i][0] <= curr_end:
                max_end = max(max_end, intervals[i][1])
                i += 1
    
            if max_end < curr_end:
                return -1
    
            cnt += 1
            curr_end = max_end + 1
    
        return cnt