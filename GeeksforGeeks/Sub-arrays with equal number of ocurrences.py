from collections import defaultdict
class Solution:
    def sameOccurrence(self, arr, x, y):
        # code here
        diff_map = defaultdict(int)
        diff_map[0] = 1 
        
        diff = 0 
        cnt_subarrays = 0
        
        for num in arr:

            if num == x:
                diff += 1
            elif num == y:
                diff -= 1
            
            cnt_subarrays += diff_map[diff]
            
            diff_map[diff] += 1
        
        return cnt_subarrays