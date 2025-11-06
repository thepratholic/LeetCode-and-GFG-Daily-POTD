from collections import defaultdict
from typing import List
from sortedcontainers import SortedSet


class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def findUPar(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def find(self, u, v):
        return self.findUPar(u) == self.findUPar(v)

    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v: return
        elif self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]

        elif self.size[ulp_v] < self.size[ulp_u]:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += 1


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        dsu = DSU(c)

        for u, v in connections:
            dsu.unionBySize(u, v)

        adj = defaultdict(SortedSet)
        online = set(range(1, c + 1))

        for station in range(1, c + 1):
            par = dsu.findUPar(station)
            adj[par].add(station)

        res = []
        for type, x in queries:

            if type == 1:
                par = dsu.findUPar(x)

                if x in adj[par]:
                    res.append(x)

                elif len(adj[par]) > 0:
                    res.append(adj[par][0])

                else:
                    res.append(-1)

            else:
                par = dsu.findUPar(x)
                adj[par].discard(x)

        return res