from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)

        adj_matrix = [[float('inf')] * 26 for _ in range(26)]

        for i in range(len(original)):
            s = ord(original[i]) - ord('a')
            t = ord(changed[i]) - ord('a')
            adj_matrix[s][t] = min(adj_matrix[s][t], cost[i])

        # applying floyd warshall
        for via in range(26):
            for i in range(26):
                for j in range(26):

                    adj_matrix[i][j] = min(adj_matrix[i][j], adj_matrix[i][via] + adj_matrix[via][j])

        
        ans = 0
        for i in range(n):
            if source[i] == target[i]:
                continue

            if adj_matrix[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')] == float('inf'):
                return -1

            ans += adj_matrix[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')]

        return ans