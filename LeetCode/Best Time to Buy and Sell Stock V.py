from typing import List


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        # def f(i, k, case):
        #     if i >= n:
        #         if case == 0: return 0
        #         else: return float('-inf')

        #     if dp[i][k][case] != -1:
        #         return dp[i][k][case]

        #     not_take = f(i + 1, k, case)
        #     take = float('-inf')

        #     if k > 0:
        #         if case == 1:
        #             take = prices[i] + f(i + 1, k - 1, 0)

        #         elif case == 2:
        #             take = -prices[i] + f(i + 1, k - 1, 0)

        #         else:
        #             take = max(-prices[i] + f(i + 1, k, 1), prices[i] + f(i + 1, k, 2))

        #     dp[i][k][case] = max(not_take, take)
        #     return dp[i][k][case]
        
        dp = [[[0] * 3 for _ in range(k + 1)] for _ in range(n + 1)]

        # return f(0, k, 0)

        for k_ in range(k + 1):
            dp[n][k_][0] = 0
            dp[n][k_][1] = float('-inf')
            dp[n][k_][2] = float('-inf')

        
        for i in range(n - 1, -1, -1):
            for k_ in range(k, -1, -1):
                for case in range(2, -1, -1):

                    not_take = dp[i + 1][k_][case]

                    take = float('-inf')

                    if k_ > 0:
                        if case == 1:
                            take = prices[i] + dp[i + 1][k_ - 1][0]

                        elif case == 2:
                            take = -prices[i] + dp[i + 1][k_ - 1][0]

                        else:
                            take = max(-prices[i] + dp[i + 1][k_][1], prices[i] + dp[i + 1][k_][2])

                    
                    dp[i][k_][case] = max(take, not_take)

        return dp[0][k][0]