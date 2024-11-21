from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        n = len(prices)
        maxi = 0

        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                maxi += prices[i] - prices[i-1]

        return maxi