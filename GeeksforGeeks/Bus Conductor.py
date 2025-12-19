class Solution:
    def findMoves(self, chairs, passengers):
        
        n = len(chairs)
        
        ans = 0
        
        chairs.sort()
        passengers.sort()
        
        for i in range(n):
            ans += abs(chairs[i] - passengers[i])
            
        return ans
        
