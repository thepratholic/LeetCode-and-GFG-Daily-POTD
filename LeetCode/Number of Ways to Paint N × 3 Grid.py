from functools import lru_cache


class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = (10 ** 9) + 7
        colors = [0, 1, 2]

        @lru_cache(None)
        def f(i, p1, p2, p3):
            
            if i == n:
                return 1

            ans = 0

            for c1 in colors:

                if c1 == p1:
                    continue

                for c2 in colors:
                    if c2 == c1 or c2 == p2:
                        continue

                    for c3 in colors:
                        if c3 == c2 or c3 == p3:
                            continue

                        ans = (ans + f(i + 1, c1, c2, c3)) % MOD

            return ans

        return f(0, -1, -1, -1)