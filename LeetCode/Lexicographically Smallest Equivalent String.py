from collections import defaultdict

class Solution:
    def dfs(self, adj, ch, vis):
        vis[ord(ch) - ord("a")] = True
        mini = ch

        for v in adj[ch]:
            if not vis[ord(v) - ord("a")]:
                candidate = self.dfs(adj, v, vis)
                if candidate < mini:
                    mini = candidate

        return mini

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        adj = defaultdict(list)

        for u, v in zip(s1, s2):
            adj[u].append(v)
            adj[v].append(u)

        result = []

        for ch in baseStr:
            vis = [False] * 26
            smallest_char = self.dfs(adj, ch, vis)
            result.append(smallest_char)

        return ''.join(result)
