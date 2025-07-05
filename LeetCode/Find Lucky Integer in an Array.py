from typing import Counter, List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)

        maxi = float("-inf")

        for k, v in freq.items():
            if k == v:
                maxi = max(maxi, k)

        return maxi if maxi != float("-inf") else -1