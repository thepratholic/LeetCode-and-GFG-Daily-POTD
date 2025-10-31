from collections import defaultdict, deque

class Solution:
    def bfs(self, start, adj, n):
        distance = [float('inf')] * n
        q = deque()
        q.append((start, -1)) # node, parent
        distance[start] = 0

        min_cycle = float('inf')
        while q:
            current_node, parent = q.popleft()

            for adjNode in adj[current_node]:
                if distance[adjNode] == float('inf'):
                    distance[adjNode] = distance[current_node] + 1
                    q.append((adjNode, current_node))

                elif adjNode != parent:
                    cycle_len = distance[current_node] + distance[adjNode] + 1
                    min_cycle = min(min_cycle, cycle_len)

        return min_cycle
        
        
    def shortCycle(self, n, edges):
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        shortest = float('inf')
        for start in range(n):
            cycle_length = self.bfs(start, adj, n)
            shortest = min(shortest, cycle_length)

        return shortest if shortest != float('inf') else -1