from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        pref = [0] * n
        pref[0] = prices[0] * strategy[0]

        pref_price = [0] * n
        pref_price[0] = prices[0]

        for i in range(1, n):
            pref[i] = pref[i - 1] + (prices[i] * strategy[i])
            pref_price[i] = pref_price[i - 1] + prices[i]

        original_sum = pref[-1]
        ans = original_sum
        r = 0
        l = 0
        while l + k - 1 < n:
            r = l + k - 1
            mid = l + k // 2

            if l > 0:
                old = pref[r] - pref[l - 1]
            else:
                old = pref[r]

            if mid > 0:
                new = pref_price[r] - pref_price[mid - 1]
            else:
                new = pref_price[r]

            delta = new - old
            ans = max(ans, original_sum + delta)

            l += 1

        return ans