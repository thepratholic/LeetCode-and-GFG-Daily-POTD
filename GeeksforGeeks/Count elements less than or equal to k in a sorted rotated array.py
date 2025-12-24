from bisect import *

class Solution:
    def countLessEqual(self, arr, x):
        
        n = len(arr)
        arr.sort()
        idx = bisect_right(arr, x)
        
        return idx