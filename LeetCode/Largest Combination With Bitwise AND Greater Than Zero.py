from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:

        bitsCount = [0] * 24
        for i in range(24):
            for j in candidates:
                if (j & (1 << i)) != 0:
                    bitsCount[i] += 1

        return max(bitsCount)
