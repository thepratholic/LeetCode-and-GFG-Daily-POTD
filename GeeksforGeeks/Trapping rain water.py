class Solution:
    def maxWater(self, arr):
        # code here
        res = 0
        n = len(arr)
        lMax = [0] * n
        rMax = [0] * n
        
        lMax[0] = arr[0]
        for i in range(1, n):
            lMax[i] = max(lMax[i-1], arr[i])
            
        rMax[n-1] = arr[n-1]
        for i in range(n-2, -1, -1):
            rMax[i] = max(rMax[i+1], arr[i])
        
        for i in range(1, n-1):
            res += (min(rMax[i], lMax[i]) - arr[i])
        
        return res
