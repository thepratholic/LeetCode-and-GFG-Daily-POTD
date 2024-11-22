class Solution:
    def maximumProfit(self, prices):
        # code here
        n = len(prices)
        mini, profit = prices[0], 0

        for i in range(1, n):
            cost = prices[i] - mini
            profit = max(profit, cost)
            mini = min(mini, prices[i])

        return profit