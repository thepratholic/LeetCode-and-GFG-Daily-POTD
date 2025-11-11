from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        # size = len(strs)

        # def f(idx, zeros, ones):
        #     if idx >= size:
        #         return 0

        #     if dp[idx][zeros][ones] != -1:
        #         return dp[idx][zeros][ones]

        #     not_taken = f(idx + 1, zeros, ones)

        #     # now, the taken part will come
        #     z = strs[idx].count('0')
        #     o = strs[idx].count('1')

        #     taken = 0
        #     if zeros + z <= m and ones + o <= n:
        #         taken = 1 + f(idx + 1, zeros + z, ones + o)

        #     dp[idx][zeros][ones] = max(taken, not_taken)
        #     return dp[idx][zeros][ones]

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # return f(0, 0, 0)

        for s in strs:
            z = s.count('0')
            o = s.count('1')

            for zeros in range(m, z - 1, -1):
                for ones in range(n, o - 1, -1):
                    
                    not_taken = dp[zeros][ones]

                    taken = 1 + dp[zeros - z][ones - o]

                    dp[zeros][ones] = max(taken, not_taken)

        return dp[m][n]