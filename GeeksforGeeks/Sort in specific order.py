class Solution:
    def sortIt(self, arr):
        n = len(arr)
        
        i, j = 0, n - 1
        
        while i < j:
            
            if arr[i] % 2 == 0 and arr[j] & 1:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
                
            elif arr[i] & 1:
                i += 1
                
            elif arr[j] % 2 == 0:
                j -= 1
                
                
        
        last_odd = -1
        
        for i in range(n):
            if arr[i] & 1:
                last_odd = i
                
        
        arr[:last_odd + 1] = sorted(arr[:last_odd + 1], reverse=True)
        arr[last_odd + 1:] = sorted(arr[last_odd + 1:])

        return arr