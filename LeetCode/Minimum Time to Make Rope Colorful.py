from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)

        if n == 1:
            return 0


        def f(idx):
            if idx >= n:
                return 0

            if colors[idx] == colors[idx - 1]:
                remove = min(neededTime[idx - 1], neededTime[idx])
                carry = max(neededTime[idx - 1], neededTime[idx])
                neededTime[idx] = carry
                return remove + f(idx + 1)
            else:
                return f(idx + 1)

        return f(1)