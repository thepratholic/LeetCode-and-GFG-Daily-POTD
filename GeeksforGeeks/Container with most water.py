class Solution:
    def maxWater(self, arr):
        # code here
        
        ans = 0
        i, j = 0, len(arr)-1
        
        while i < j:
            current = min(arr[i], arr[j]) * (j-i)
            
            ans = max(ans, current)
            
            if arr[i] < arr[j]:
                i += 1
            else:
                j -= 1
                
        return ans