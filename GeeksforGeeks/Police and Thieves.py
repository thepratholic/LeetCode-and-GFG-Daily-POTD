class Solution:
    def catchThieves(self, arr, k):
        n = len(arr)
        
        police = []
        thief = []
        
        for i in range(n):
            if arr[i] == 'T':
                thief.append(i)
                
            else:
                police.append(i)
                
                
        i, j = 0, 0
        ans = 0
        
        while i < len(police) and j < len(thief):
            
            if abs(police[i] - thief[j]) <= k:
                ans += 1
                i += 1
                j += 1
                
            elif police[i] < thief[j]:
                i += 1
                
            else:
                j += 1
                
        return ans