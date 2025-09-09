MOD = 10**9 + 7
class Solution:

    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        dp = [0] * (n + 1)
        dp[1] = 1

        for day in range(2, n + 1):
            ans = 0
            for d in range(day - forget + 1, day - delay + 1):
                if d > 0:
                    ans = (ans + dp[d]) % MOD
                
            dp[day] = ans % MOD

        total = 0
        for day in range(n - forget + 1, n + 1):
            total = (total + dp[day]) % MOD

        return total