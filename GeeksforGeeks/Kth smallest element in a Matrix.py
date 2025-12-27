import heapq
class Solution:
    def kthSmallest(self, mat, k):
        
        n = len(mat)
        
        pq = []
        
        for i in range(n):
            for j in range(n):
                heapq.heappush(pq, mat[i][j])
                
        
        ans = -1
        while k > 0:
            
            ans = heapq.heappop(pq)
            k -= 1
            
        return ans