class Solution:
    def minWindow(self, s1, s2):
        
        n, m = len(s1), len(s2)
        
        
        i = 0
        ans = ""
        mini = float('inf')
        
        while i < n:
            j = 0
            
            while i < n:
                if s1[i] == s2[j]:
                    j += 1
                    
                    if j == m: break
                i += 1
                
            
            if j < m:
                break
            
            end = i
            j = m - 1
            
            while j >= 0:
                if s1[i] == s2[j]:
                    j -= 1
                    
                i -= 1
                
            i += 1
            
            if end - i + 1 < mini:
                mini = end - i + 1
                ans = s1[i:end + 1]
                
            i += 1
            
        return ans