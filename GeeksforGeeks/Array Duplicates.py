from collections import Counter
class Solution:
    def findDuplicates(self, arr):
        
        n = len(arr)
        ans = []
        
        freq = Counter(arr)
        
        for k, v in freq.items():
            if v > 1:
                ans.append(k)
                
        return ans
        