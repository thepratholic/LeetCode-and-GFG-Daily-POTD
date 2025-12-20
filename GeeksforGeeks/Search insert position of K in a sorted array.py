class Solution:
    def searchInsertK(self, arr, k):
        
        n = len(arr)
        
        low, high = 0, n - 1
        
        ans = n
        
        while low <= high:
            mid = (low + high) >> 1
            
            if arr[mid] == k:
                return mid

            
            elif arr[mid] < k:
                low = mid + 1
                
            else:
                ans = mid
                high = mid - 1
                
                
        return ans