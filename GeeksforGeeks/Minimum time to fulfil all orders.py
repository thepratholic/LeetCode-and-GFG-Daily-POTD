class Solution:
    def minTime(self, ranks, n):
        m = len(ranks)
        
        def check(mid):
            donuts = 0
            
            for r in ranks:
                k = 1
                cur_time = 0
                
                while cur_time + r * k <= mid:
                    donuts += 1
                    cur_time += r * k
                    k += 1
                    
                if donuts >= n:
                    return True
                    
            return False
            
            
        ans = -1
        low, high = 0, int(1e8)
        
        while low <= high:
            mid = (low + high) // 2
            
            if check(mid):
                ans = mid
                high = mid - 1
                
            else:
                low = mid + 1
                
        return ans