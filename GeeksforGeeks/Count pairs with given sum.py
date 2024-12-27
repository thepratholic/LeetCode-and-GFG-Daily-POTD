class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        #Your code here
        mpp = {}
        cnt = 0
        n = len(arr)
        
        for num in arr:
            c = target - num
            
            if c in mpp:
                cnt += mpp[c]
                
            if num not in mpp:
                mpp[num] = 1
            else:   
                mpp[num] += 1
            
        return cnt