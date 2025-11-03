from collections import defaultdict, deque

class Solution:
    def safeNodes(self, V, edges):
        adj = defaultdict(list)
        
        out = [0] * V
        
        for u, v in edges:
            adj[v].append(u)
            out[u] += 1
            
        
        
        q = deque()
        
        for node in range(len(out)):
            if out[node] == 0:
                q.append(node)
        
        ans = []    
        while q:
            cur = q.popleft()
            ans.append(cur)
            
            for adjNode in adj[cur]:
                
                out[adjNode] -= 1
                
                if out[adjNode] == 0:
                    q.append(adjNode)
                    
                    
        ans.sort()
        return ans