class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        
        leftsum = 0
        rightsum = sum(arr)
        
        n = len(arr)
        
        for i in range(n):
            
            rightsum -= arr[i]
            
            if leftsum == rightsum:
                return i
            leftsum += arr[i]
                
                
        return -1