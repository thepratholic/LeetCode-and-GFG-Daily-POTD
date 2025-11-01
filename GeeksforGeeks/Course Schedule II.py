from collections import defaultdict, deque

class Solution:
    def findOrder(self, n, prerequisites):
        
        adj = defaultdict(list)
        indegree = [0] * n
        
        for x, y in prerequisites:
            adj[y].append(x)
            indegree[x] += 1
            
        
        order = []
        
        q = deque()
        
        for node in range(n):
            if indegree[node] == 0:
                q.append(node)
                
        
        while q:
            cur_node = q.popleft()
            order.append(cur_node)
            
            for adjNode in adj[cur_node]:
                
                indegree[adjNode] -= 1
                
                if indegree[adjNode] == 0:
                    q.append(adjNode)
                    
        return order