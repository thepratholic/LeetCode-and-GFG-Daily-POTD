from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, 2 * w))

        pq = []
        dist = [float('inf')] * n
        heappush(pq, (0, 0)) # distance, node
        dist[0] = 0

        while pq:
            cur_dist, cur_node = heappop(pq)

            for adjNode, wt in adj[cur_node]:
                if dist[adjNode] == float('inf') or dist[adjNode] > cur_dist + wt:
                    heappush(pq, (cur_dist + wt, adjNode))
                    dist[adjNode] = min(dist[adjNode], cur_dist + wt)

        return -1 if dist[-1] == float('inf') else dist[-1] 