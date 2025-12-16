from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)

        if n == 1: return 1

        ans = n

        i = 0
        while i < n:

            j = i + 1
            while j < n and prices[j - 1] - prices[j] == 1:
                j += 1

            l = j - i
            ans += (l * (l - 1) // 2)

            i = j

        return ans