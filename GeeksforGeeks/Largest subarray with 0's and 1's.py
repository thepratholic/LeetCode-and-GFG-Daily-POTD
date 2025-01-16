class Solution:
    def maxLen(self, arr):
        # code here
        
        longest = 0
        n = len(arr)
        
        mpp = {}
        sum = 0
        
        for i in range(n):
            
            if arr[i] == 0:
                sum -= 1
            else:
                sum += 1
                
            if sum == 0:
                longest = max(longest, i+1)
                
            if sum in mpp:
                longest = max(longest, i - mpp[sum])
                
            else:
                mpp[sum] = i
                
        return longest