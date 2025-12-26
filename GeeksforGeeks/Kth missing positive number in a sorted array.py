class Solution:
    def kthMissing(self, arr, k):
        
        st = set(arr)
        
        num = 1
        
        while k > 0:
            if num in st:
                num += 1
                
            else:
                num += 1
                k -= 1
                
        return num - 1