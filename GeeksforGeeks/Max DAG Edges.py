class Solution:
    def maxEdgesToAdd(self, V, edges):
        
        total = V * (V - 1) // 2
        return total - len(edges)