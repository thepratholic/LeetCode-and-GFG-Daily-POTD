class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self,s):
        #code here
        hash = {}
        
        for i in s:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
                
                
        for k, v in hash.items():
            if v == 1:
                return k
                
        return -1