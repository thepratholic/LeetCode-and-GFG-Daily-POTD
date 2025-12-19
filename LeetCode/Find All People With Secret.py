from typing import List


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def findUPar(self, x):
        if self.parent[x] == x:
            return x

        self.parent[x] = self.findUPar(self.parent[x])
        return self.parent[x]

    def find(self, u, v):
        return self.findUPar(u) == self.findUPar(v)

    def unionBySize(self, u, v):
        ulp_u, ulp_v = self.findUPar(u), self.findUPar(v)
        if ulp_u == ulp_v: return
        elif self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]

        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

    def reset(self, u):
        self.parent[u] = u
        self.size[u] = 1

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        dsu = DSU(n)
        meetings.sort(key = lambda x : x[2])
        
        dsu.unionBySize(0, firstPerson)

        i = 0

        while i < len(meetings):
            cur_time = meetings[i][2]

            cur_people = []

            while i < len(meetings) and meetings[i][2] == cur_time:
                dsu.unionBySize(meetings[i][0], meetings[i][1])
                cur_people.append(meetings[i][0])
                cur_people.append(meetings[i][1])

                i += 1

            for cur in cur_people:
                if dsu.findUPar(cur) != dsu.findUPar(0):
                    dsu.reset(cur)

        ans = []
        for i in range(n):
            if dsu.findUPar(i) == dsu.findUPar(0):
                ans.append(i)

        return ans