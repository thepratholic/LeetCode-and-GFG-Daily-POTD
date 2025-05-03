from typing import List


class Solution:
    def find(self, tops, bottoms, value):
        swapTop, swapBottom = 0, 0
        for i in range(len(tops)):
            if tops[i] != value and bottoms[i] != value:
                return -1

            elif tops[i] != value:
                swapTop += 1
            
            elif bottoms[i] != value:
                swapBottom += 1

        return min(swapTop, swapBottom)

    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        ans = float("inf")

        for value in range(1, 7):
            currentSwaps = self.find(tops, bottoms, value)
            if currentSwaps != -1:
                ans = min(ans, currentSwaps)

        return ans if ans != float("inf") else -1